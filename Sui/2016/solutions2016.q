// solutions
.aoc.201601part1: {l:{x[0],"J"$1_x} each ", " vs raze x;
                   .aoc.d1:("NR";"NL";"SR";"SL";"WR";"WL";"ER";"EL")!"EWWENSSN";
                   .aoc.d2:"NSWE"!({0,x};{0,neg[x]};{neg[x],0};{x,0});
                   sum abs last ("N";0 0){f,enlist x[1] + (.aoc.d2 f:.aoc.d1 x[0],y[0]) y[1]}/l};
.aoc.201601part2: {l:{x[0],"J"$1_x} each ", " vs raze x;
                   .aoc.d1:("NR";"NL";"SR";"SL";"WR";"WL";"ER";"EL")!"EWWENSSN";
                   .aoc.d2:"NSWE"!({0,x};{0,neg[x]};{neg[x],0};{x,0});
                   c:(enlist 0 0),last each ("N";0 0){f,enlist x[1] + (.aoc.d2 f:.aoc.d1 x[0],y[0]) y[1]}\l;
                   f:{$[0=first d:where not x=y;
                      (s[1]+til 1+(-/)s:desc raze (x;y) @\: d) ,' first y where x=y;
                      (first y where x=y) ,' s[1]+til 1+(-/)s:desc raze (x;y) @\: d]};
                   .aoc.p:enlist 0 0; i:0;
                   while[(count .aoc.p)=count distinct .aoc.p;.aoc.p,:f[c[i];c[i+1]] except enlist c[i];i+:1];
                   sum abs last where 1<count each group .aoc.p};
.aoc.201602part1: {.aoc.f2:{$[y="U";$[x>3;x-3;x];y="D";$[x<7;x+3;x];y="L";$[1=x mod 3;x;x-1];$[0=x mod 3;x;x+1]]};
                   "J"$"" sv string 5 {x .aoc.f2/ y}\ x};
.aoc.201602part2: {.aoc.f2:{$[y="U";$[x in 1 2 4 5 9;x;x in 3 13;x-2;x-4];y="D";$[x in 5 9 10 12 13;x;x in 1 11;x+2;x+4];
                              y="L";$[x in 1 2 5 10 13;x;x-1];$[x in 1 4 9 12 13;x;x+1]]};
                   upper last each string `byte$5 {x .aoc.f2/ y}\ x};
.aoc.201603part1: {sum 0>(-/') desc each {l where not null l:"J"$" " vs x} each x};
.aoc.201603part2: {sum 0>(-/') desc each raze flip each 3 cut {l where not null l:"J"$" " vs x} each x};
.aoc.201604part1: {sum {"J"$-7_last "-" vs x} each x where {(-1_-6#x)~5#key desc count each group asc "" sv -1 _ "-" vs x} each x};
.aoc.201604part2: {.aoc.decrypt:{.Q.a ((y mod 26)+.Q.a?x) mod 26};
                   "J"$-7_last "-" vs first x where (" " sv' {.aoc.decrypt[;"J"$-7_last "-" vs x] each -1 _ "-" vs x} each x) like "*north*"};
.aoc.201605part1: {p:{i:x+1; while[not "00000" ~ 5#"" sv string (md5 (raze y),string i)[til 3];i+:1]; i}[;x]\[8;0];
                   ({"" sv x} each string md5 each (raze x),/:string 1_p)[;5]};
.aoc.201605part2: {p:{i:x[0]+1; n:x[1]; while[or[not (last l) in n; not "00000" ~ 5#l:"" sv string (md5 (raze y),string i)[til 3]];i+:1]; (i;n except last l)}[;x]\[8;(0;"01234567")];
                   c:({"" sv x} each string md5 each (raze x),/:string 1_p[;0]) [;5 6];
                   @[8#" ";"J"$'c[;0];:;c[;1]]};


// calculate and profile
problem:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs problem;func:f;0N!"No function matches"];
$[(input_file:`$ssr[problem;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"No input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;$[1<count raw_input;enlist raw_input;raw_input]];
  0N!"Result of ",problem,": ", $[10h=type r 1;r 1;string r 1];
  0N!"Time usage in milliseconds ",string r[0;0];
  0N!"Space usage in bytes ",string r[0;1]];
