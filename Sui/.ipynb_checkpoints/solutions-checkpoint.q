// solutions

.aoc.201501part1: {(-/)sum each "()" =\: raze x};
.aoc.201501part2: {first where 0>(+\)0,("()"!1 -1) x};
.aoc.201502part1: {sum {(prd 2#asc l)+sum neg[l*l], prd each l cross l:"J"$"x" vs x} each x};
.aoc.201502part2: {sum {(prd l)+2*sum 2#asc l:"J"$"x" vs x} each x};
.aoc.201503part1: {count distinct (+\)(enlist 0 0),("^v<>"!(0 1;0 -1;-1 0;1 0)) raze x};
.aoc.201503part2: {count distinct raze (+\')(enlist 0 0),/:l where each 0 1 =\: (til count l:("^v<>"!(0 1;0 -1;-1 0;1 0)) raze x) mod 2};
.aoc.201504part1: {i:0;while[not (5#raze string md5 (raze x),string i) ~ "00000";i+:1];i};
.aoc.201504part2: {i:0;while[not (6#raze string md5 (raze x),string i) ~ "000000";i+:1];i};
.aoc.201505part1: {c1:{3<=sum max "aeiou" =\: x};
                   c2:{any (=/) -1 1 _\: x};
                   c3:{not any x like/: "*",/:("ab";"cd";"pq";"xy"),\:"*"};
                   sum {[c1;c2;c3;s]$[all (c1;c2;c3) @\: s;1;0]}[c1;c2;c3;] each x};
.aoc.201505part2: {c1:{and[any 1<count each ss[x;]each(key d) where value d;
                       any d:1<count each group l where 2=count each l:(2 cut x),2 cut 1_x]};
                   c2:{any (=/) 2 -2 _\: x};
                   sum {[c1;c2;s]$[all (c1;c2) @\: s;1;0]}[c1;c2;] each x};
.aoc.201506part1: {.aoc.d6:(l cross l:til 1000)!1000000#-1;
                   f:{i:$[x like "turn on*";`on;x like "turn off*";`off;`to];
                      g:(cross/) {x[0]+til 1+abs(-/)x} each flip "J"$"," vs' (" " vs x) $[i=`to;1 3;2 4];
                      $[i=`on;@[`.aoc.d6;g;:;1];i=`off;@[`.aoc.d6;g;:;-1];@[`.aoc.d6;g;neg]]};
                   f each x; sum 1=value .aoc.d6};
.aoc.201506part2: {.aoc.d6:(l cross l:til 1000)!1000000#0;
                   f:{i:$[x like "turn on*";`on;x like "turn off*";`off;`to];
                      g:(cross/) {x[0]+til 1+abs(-/)x} each flip "J"$"," vs' (" " vs x) $[i=`to;1 3;2 4];
                      $[i=`on;@[`.aoc.d6;g;+;1];i=`to;@[`.aoc.d6;g;+;2];@[`.aoc.d6;g;{$[x>0;x-:1;x:0]}]]};
                   f each x; sum value .aoc.d6};


// calculate and profile
p:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs p;func:f;0N!"No function matches"];
$[(input_file:`$ssr[p;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"No input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;$[1<count raw_input;enlist raw_input;raw_input]];
  0N!"Result of ",p,": ", string r 1;
  0N!"Time usage in milliseconds ",string r[0;0];
  0N!"Space usage in bytes ",string r[0;1]];