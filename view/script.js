// https://observablehq.com/@d3/force-directed-graph@149
function getWeight(src,tgt){
  let srcfirst2octet = src.slice(0,8);
  let tgtfirst2octet = tgt.slice(0,8);
  let main2octet = "118.229.";

  if(srcfirst2octet == tgtfirst2octet && srcfirst2octet == main2octet){
    return 2;
  }
  if((srcfirst2octet == "118" && tgtfirst2octet != "118") || (srcfirst2octet != "118" && tgtfirst2octet == "118")){
    return 0.5;
  }
  else{
    return 1;
  }
}

function getStrength(src,tgt){
  let srcfirst2octet = src.slice(0,8);
  let tgtfirst2octet = tgt.slice(0,8);
  let main2octet = "118.229.";
  if(srcfirst2octet == tgtfirst2octet && srcfirst2octet == main2octet){
    
    return 1;
  }
  if((srcfirst2octet == main2octet && tgtfirst2octet !=main2octet) || (srcfirst2octet != main2octet && tgtfirst2octet == main2octet)){
    return 5;
  }
  else{
    return 3;
  }
}

export default function define(runtime, observer) {
  const main = runtime.module();
  const fileAttachments = new Map([
    ["data.json", new URL("./data_for_d3js.json", import.meta.url)],
  ]);
  main.builtin(
    "FileAttachment",
    runtime.fileAttachments((name) => fileAttachments.get(name))
  );

  main
    .variable(observer("chart"))
    .define(
      "chart",
      ["data", "d3", "width", "height", "color", "drag", "invalidation"],
      function (data, d3, width, height, color, drag, invalidation) {

        const links = data.links.map((d) => Object.create(d));
        const nodes = data.nodes.map((d) => Object.create(d));

        const simulation = d3
          .forceSimulation(nodes)
          .force(
            "link",
            d3.forceLink(links).id((d) => d.id)
            .distance(function (d) {
              //length scales with distance
              return (getWeight(d.source.id, d.target.id))/50 | 20;
            })
            .strength(function (d) {
              //length scales with distance
              return (getStrength(d.source.id, d.target.id))/50;
            })
          )
          .force("charge", d3.forceManyBody().strength(-3))
          .force("center", d3.forceCenter(width / 2, height / 2));

        const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]);

        const link = svg
          .append("g")
          .attr("stroke", "#999")
          .attr("stroke-opacity", 0.6)
          .selectAll("line")
          .data(links)
          .join("line")
          .attr("stroke-width", (d) => Math.sqrt(d.value));

        const node = svg
          .append("g")
          .attr("stroke", "#fff")
          .attr("stroke-width", 1.5)
          .selectAll("circle")
          .data(nodes)
          .join("circle")
          .attr("r", 5)
          .attr("fill", color)
          .call(drag(simulation));

        node.append("title")
            .text((d) => d.id)
            .style("text-anchor", "middle")
            .style("fill", "#555")
            .style("font-family", "Arial")
            .style("font-size", 12);


        simulation.on("tick", () => {
          link
            .attr("x1", (d) => d.source.x)
            .attr("y1", (d) => d.source.y)
            .attr("x2", (d) => d.target.x)
            .attr("y2", (d) => d.target.y);

          node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
        });

        invalidation.then(() => simulation.stop());

        return svg.node();
      }
    );
  main
    .variable(observer("data"))
    .define("data", ["FileAttachment"], function (FileAttachment) {
      return FileAttachment("data.json").json();
    });
  main.variable(observer("height")).define("height", function () {
    return 1200;
  });
  main.variable(observer("color")).define("color", ["d3"], function (d3) {
    const scale = d3.scaleOrdinal(d3.schemeCategory10);
    return (d) => scale(d.group);
  });
  main.variable(observer("drag")).define("drag", ["d3"], function (d3) {
    return (simulation) => {
      function dragstarted(event) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
      }

      function dragged(event) {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
      }

      function dragended(event) {
        if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
      }

      return d3
        .drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
    };
  });
  main.variable(observer("d3")).define("d3", ["require"], function (require) {
    return require("d3@6");
  });
  return main;
}
