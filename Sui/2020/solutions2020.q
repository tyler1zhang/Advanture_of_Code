// solutions
.aoc.202001part1:{prd l where (2020 - l) in l:"J"$x};
.aoc.202001part2:{first r where not null r:distinct {if[2=sum b:((2020 - y[x]) - l) in l:y _ x; :prd y[x],l where b]}[;l] each til count l:"J"$x};


// calculate and profile
problem:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs problem;func:f;0N!"No function matches"];
$[(input_file:`$ssr[problem;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"No input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;$[1<count raw_input;enlist raw_input;raw_input]];
  0N!"Result of ",problem,": ", $[10h=type r 1;r 1;string r 1];
  0N!"Time usage in milliseconds ",string r[0;0];
  0N!"Space usage in bytes ",string r[0;1]];
