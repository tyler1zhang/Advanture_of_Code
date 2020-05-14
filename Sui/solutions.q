// solutions

.aoc.201501part1: {(-/)sum each "()" =\: raze x};
.aoc.201501part2: {first where 0>(+\)0,("()"!1 -1) x};
.aoc.201502part1: {sum {(prd 2#asc l) + sum neg[l * l], prd each l cross l:"J"$"x" vs x} each x};


// calculate and profile
p:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs p;func:f;0N!"No function matches"];
$[(input_file:`$ssr[p;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"No input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;$[1<count raw_input;enlist raw_input;raw_input]];
  0N!"Result of ",p,": ", string r 1;
  0N!"Time usage in milliseconds ",string r[0;0];
  0N!"Space usage in bytes ",string r[0;1]];
