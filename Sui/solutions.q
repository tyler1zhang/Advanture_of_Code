// solutions

.aoc.201501part1: {(-/)sum each "()" =\: raze x};
.aoc.201501part2: {first where 0>(+\)0,("()"!1 -1) x};


// calculate and profile
p:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs p;func:f;0N!"No function matches"];
$[(input_file:`$ssr[p;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"no input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;raw_input];
  0N!"result of ",p,": ", string r 1;
  0N!"time usage in milliseconds ",string r[0;0];
  0N!"space usage in bytes ",string r[0;1]];
