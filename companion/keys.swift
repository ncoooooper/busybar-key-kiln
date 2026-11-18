import Foundation
import CoreGraphics
guard CommandLine.arguments.count==2 else {fputs("usage: swift keys.swift COUNTS.json\n",stderr);exit(2)}
let file=URL(fileURLWithPath:NSString(string:CommandLine.arguments[1]).expandingTildeInPath)
struct Bucket:Codable {var count:Int;var minutes:[Int]}
let fmt=DateFormatter();fmt.locale=Locale(identifier:"en_US_POSIX");fmt.timeZone = .current;fmt.dateFormat="yyyy-MM-dd"
var counts=((try? Data(contentsOf:file)).flatMap {try? JSONDecoder().decode([String:Bucket].self,from:$0)}) ?? [:]
var previous=CGEventSource.counterForEventType(.combinedSessionState,eventType:.keyDown)
var previousDay=fmt.string(from:Date())
let tick=Timer.scheduledTimer(withTimeInterval:1,repeats:true) {_ in
 let now=Date(),day=fmt.string(from:now),current=CGEventSource.counterForEventType(.combinedSessionState,eventType:.keyDown)
 let delta=current>=previous && previousDay==day ? Int(current-previous):0
 previous=current;previousDay=day
 if delta>0 || counts[day]==nil {
  var bucket=counts[day] ?? Bucket(count:0,minutes:[])
  let minute=Int(now.timeIntervalSince1970/60);if delta>0 && bucket.minutes.last != minute {bucket.minutes.append(minute)}
  bucket.count += delta;counts[day]=bucket
  do {try JSONEncoder().encode(counts).write(to:file,options:.atomic)} catch {fputs("Cannot save counts\n",stderr)}
 }
}
RunLoop.current.run()
