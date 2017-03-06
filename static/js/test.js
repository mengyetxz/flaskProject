/**
 * Created by mengy on 2017/3/2.
 */
var theData = [1, 2, 3];

var p = d3.select("body")
    .data(theData)
    .enter()
    .append("p")
    .text("hello");