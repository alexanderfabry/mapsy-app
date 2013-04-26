function mapsylog(message) {
  $("div#log").text("[DEV INFO]: "+message);
}

function mapsy() {

  var width = 1024;
  var height = 500;

  var projection = d3.geo.mercator()
      .center([0,60])
      .scale(300)
      .rotate([0,0]);

  var svg = d3.select("svg")
      .attr("width", width)
      .attr("height", height);

  var path = d3.geo.path()
      .projection(projection);

  var g = svg.append("g");

  // load and display the World
  d3.json("world-110m2.json", function(error, topology) {

    // setup the actions triggered on mouse events
    // prepare the div element for display
    var div = d3.select("body")
                .selectAll("div.artwork")
                .style("opacity", "1");

    var mapsy_calledOn_mouseMoveArtwork =  function(){ 
      div
            .text(d3.event.pageX + ", " + d3.event.pageY)
            .style("left", (d3.event.pageX + 5) + "px")
            .style("top", (d3.event.pageY + 5) + "px");
    }

    var mapsy_calledOn_mouseOverArtwork =  function(){ 
      div.transition()
            .duration(100)
            .style("opacity", 1);

      div.style("left", (d3.event.pageX - 100) + "px")     
          .style("top", (d3.event.pageY -100) + "px");
    }

    var mapsy_calledOn_mouseOutArtwork =  function(){ 
        div.transition().duration(100).style("opacity", 1e-6);
    }

    // setup map and fill it with data
    d3.csv("cities.csv", function(error, data) {
      g.selectAll("circle")
           .data(data)
           .enter()
           .append("circle")
           .attr("cx", function(d) {
                   return projection([d.lon, d.lat])[0];
           })
           .attr("cy", function(d) {
                   return projection([d.lon, d.lat])[1];
           })
           .attr("r", 15)
           .on("mouseover", mapsy_calledOn_mouseOverArtwork)
           .on("mouseout", mapsy_calledOn_mouseOutArtwork)
           .on("mousemove", mapsy_calledOn_mouseMoveArtwork)
           .style("fill", "white");
    });

    g.selectAll("path")
          .data(topojson.object(topology, topology.objects.countries)
              .geometries)
        .enter()
          .append("path")
          .attr("d", path)
    });

    // zoom and pan
    var zoom = d3.behavior.zoom()
        .on("zoom",function() {
            g.attr("transform","translate("+ 
                d3.event.translate.join(",")+")scale("+d3.event.scale+")");
            g.selectAll("circle")
                .attr("d", path.projection(projection));
            g.selectAll("path")  
                .attr("d", path.projection(projection)); 

      });

      svg.call(zoom)
};

$(document).ready(function() {
  mapsy();
  mapsylog();
});