// solutions
.aoc.202001part1:{prd l where (2020-l) in l:"J"$x};
.aoc.202001part2:{prd l where l in 2020-raze l+\:l:"J"$x};
.aoc.202002part1:{sum {(sum v[1][0]=v[2]) within "J"$"-" vs first v:" " vs x} each x};
.aoc.202002part2:{sum {1=sum v[1][0]=v[2] -1+"J"$"-" vs first v:" " vs x} each x};
.aoc.202003part1:{sum "#"=((1+3*c)#'x)./:n,'3*n:til c:count x};
.aoc.202003part2:{m:(1+7*c:count x)#'x; prd `long${sum "#"=y ./: x}[;m] each {((-1+z) div x){x+y}[;(x;y)]\0 0}[;;c] .' (1 1;1 3;1 5;1 7;2 1)};

// calculate and profile
problem:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs problem;func:f;0N!"No function matches"];
$[(input_file:`$ssr[problem;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"No input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;$[1<count raw_input;enlist raw_input;raw_input]];
  0N!"Result of ",problem,": ", $[10h=type r 1;r 1;string r 1];
  0N!"Time usage in milliseconds ",string r[0;0];
  0N!"Space usage in bytes ",string r[0;1]];
