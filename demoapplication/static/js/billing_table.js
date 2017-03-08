/**
 * Created by mengy on 2017/3/2.
 */
function createCaption() {
    var x = document.getElementsByClassName('billing-table').createCaption();
    x.innerHTML = "mytablecaption";

}

d3.text("/static/data.csv", createTable);
function createTable(data) {

    //d3.csv.parse returns an array of objects
    var parsedCSV = d3.csv.parseRows(data);
    var container = d3.select("body").selectAll("div.billing")
        .append("table")
        .attr("border", "1")

        .selectAll("tr")
        .data(parsedCSV).enter()
        .append("tr")

        .selectAll("td")
        .data(function(d) { return d; }).enter()
        .append("td")
        .text(function(d) { return d; });
}