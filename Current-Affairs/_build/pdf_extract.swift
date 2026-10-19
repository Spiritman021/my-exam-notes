import Foundation
import CoreGraphics
let path = CommandLine.arguments[1], out = CommandLine.arguments[2], maxPage = Int(CommandLine.arguments[3]) ?? 999
guard let doc = CGPDFDocument(URL(fileURLWithPath: path) as CFURL) else { exit(1) }
var count = 0
for p in 1...min(doc.numberOfPages, maxPage) {
    guard let page = doc.page(at: p), let dict = page.dictionary else { continue }
    var res: CGPDFDictionaryRef?; guard CGPDFDictionaryGetDictionary(dict, "Resources", &res), let r = res else { continue }
    var xo: CGPDFDictionaryRef?; guard CGPDFDictionaryGetDictionary(r, "XObject", &xo), let x = xo else { continue }
    var idx = 0
    CGPDFDictionaryApplyBlock(x, { key, obj, _ in
        var stream: CGPDFStreamRef?
        guard CGPDFObjectGetValue(obj, .stream, &stream), let s = stream, let sd = CGPDFStreamGetDictionary(s) else { return true }
        var sub: UnsafePointer<Int8>?
        guard CGPDFDictionaryGetName(sd, "Subtype", &sub), let st = sub, String(cString: st) == "Image" else { return true }
        var w: CGPDFInteger = 0, h: CGPDFInteger = 0
        CGPDFDictionaryGetInteger(sd, "Width", &w); CGPDFDictionaryGetInteger(sd, "Height", &h)
        var fmt = CGPDFDataFormat.raw
        guard let data = CGPDFStreamCopyData(s, &fmt) as Data? else { return true }
        idx += 1
        let name = String(format: "%@/p%02d_%02d_%dx%d", out, p, idx, w, h)
        if fmt == .jpegEncoded || fmt == .JPEG2000 {
            try? data.write(to: URL(fileURLWithPath: name + (fmt == .jpegEncoded ? ".jpg" : ".jp2")))
        } else {
            // raw samples: write as PPM if 8-bit RGB/Gray
            var bpc: CGPDFInteger = 8; CGPDFDictionaryGetInteger(sd, "BitsPerComponent", &bpc)
            let comps = data.count / max(1, Int(w*h))
            if bpc == 8 && (comps == 3 || comps == 1) {
                let hdr = (comps == 3 ? "P6" : "P5") + "\n\(w) \(h)\n255\n"
                var d = Data(hdr.utf8); d.append(data)
                try? d.write(to: URL(fileURLWithPath: name + (comps == 3 ? ".ppm" : ".pgm")))
            } else { print("skip", name, "comps", comps, "bpc", bpc) }
        }
        count += 1
        return true
    }, nil)
}
print("images:", count)
