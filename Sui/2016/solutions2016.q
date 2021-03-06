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
.aoc.201606part1: {first each key each desc each count each' group each flip x};
.aoc.201606part2: {first each key each asc each count each' group each flip x};
.aoc.201607part1: {s:{" " vs @[x;p;:;(count p:raze ss[x;]each"[]")#" "]} each x;
                   b:{any {any {and[1<count distinct x; x[0 1]~x[3 2]]} each 4 cut x} each 0 1 2 3 _\: x} each' s;
                   sum {all ({any x};{all not x}) @' x {where x=(til count y) mod 2}[;x] each 0 1} each b};
.aoc.201607part2: {s:{" " vs @[x;p;:;(count p:raze ss[x;]each"[]")#" "]} each x;
                   f:{p:raze {raze {c where {and[x[0]=x[2];not x[0]=x[1]]} each c:3 cut x} each 0 1 2 _\: x} each x where 0=(til count x) mod 2;
                      any any each (x where 1=(til count x) mod 2) like/:\: ({"*",x[1 0 1],"*"} each p)};
                   sum f each s};
.aoc.201608part1: {ins:{$[x like "rect*"; (`$v[0]), "J"$"x" vs last v:" " vs x; (`$v[1]),("J"$last "=" vs v[2]),("J"$last v:" " vs x)]} each x;
                   .aoc.m:6#enlist 50#0b;
                   f:{$[x[0]=`rect; .aoc.m[til x[2];til x[1]]:1b; x[0]=`row; .aoc.m[x[1]]:neg[x[2]] rotate .aoc.m[x[1]]; .aoc.m[;x[1]]:neg[x[2]] rotate .aoc.m[;x[1]]]};
                   f each ins; sum sum each .aoc.m};
.aoc.201608part2: {ins:{$[x like "rect*"; (`$v[0]), "J"$"x" vs last v:" " vs x; (`$v[1]),("J"$last "=" vs v[2]),("J"$last v:" " vs x)]} each x;
                   .aoc.m:6#enlist 50#0b;
                   f:{$[x[0]=`rect; .aoc.m[til x[2];til x[1]]:1b; x[0]=`row; .aoc.m[x[1]]:neg[x[2]] rotate .aoc.m[x[1]]; .aoc.m[;x[1]]:neg[x[2]] rotate .aoc.m[;x[1]]]};
                   f each ins; p:(10b!"* ") .aoc.m; show "    ",/:p,\: "    "; "above"};
.aoc.201609part1: {s:raze x; r:"";
                   while["(" in s; p:first ss[s;"("]; r,:p#s; s:p _ s; q:first ss[s;")"]; c:"J"$"x" vs -1 _ 1 _ (q+1)#s; s:(q+1) _ s; r,:raze c[1]#enlist c[0]#s; s:c[0] _ s];
                   count r,s};
.aoc.201609part2: {s:raze x;
                   f:{$[not "(" in x; count x;
                        [r:first ss[x;")"]; l:first ss[x;"("];
                         c:"J"$"x" vs -1 _ 1 _ x{(except/)til each (y+1;x)}[l;r];
                         n:c[0]; m:c[1];
                         l + (m*.z.s[n#(r+1)_x]) + (.z.s[(n+r+1)_x])]]};
                   f s};
.aoc.201610part1: {v:(i:"J"$" " vs' x where x like "value*")[;1]; b:i[;5];
                   p:value g:group b; .aoc.bot:(key g)!asc each v p; .aoc.output:(`long$())!`long$();
                   instructions:{("J"$x[1];`$x[5];"J"$x[6];`$x[10];"J"$x[11])} each " " vs' x where x like "bot*";
                   move:{if[not 2=count .aoc.bot[x[0]];:(::)]; if[17 61~.aoc.bot[x[0]];:(::)];
                         $[`bot=x[1];
                           .aoc.bot[x[2]]::asc .aoc.bot[x[2]], .aoc.bot[x[0]][0];
                           .aoc.output[x[2]]::.aoc.bot[x[0]][0]];
                         $[`bot=x[3];
                           .aoc.bot[x[4]]::asc .aoc.bot[x[4]], .aoc.bot[x[0]][1];
                           .aoc.output[x[4]]::.aoc.bot[x[0]][1]];
                         .aoc.bot[x[0]]:`long$()};
                   while[not 17 61 in value .aoc.bot; move each instructions]; .aoc.bot?17 61};
.aoc.201610part2: {v:(i:"J"$" " vs' x where x like "value*")[;1]; b:i[;5];
                   p:value g:group b; .aoc.bot:(key g)!asc each v p; .aoc.output:(`long$())!`long$();
                   instructions:{("J"$x[1];`$x[5];"J"$x[6];`$x[10];"J"$x[11])} each " " vs' x where x like "bot*";
                   move:{if[not 2=count .aoc.bot[x[0]];:(::)];
                         $[`bot=x[1];
                           .aoc.bot[x[2]]::asc .aoc.bot[x[2]], .aoc.bot[x[0]][0];
                           .aoc.output[x[2]]::.aoc.bot[x[0]][0]];
                         $[`bot=x[3];
                           .aoc.bot[x[4]]::asc .aoc.bot[x[4]], .aoc.bot[x[0]][1];
                           .aoc.output[x[4]]::.aoc.bot[x[0]][1]];
                         .aoc.bot[x[0]]:`long$()};
                   while[any null .aoc.output[0 1 2]; move each instructions]; prd .aoc.output[0 1 2]};


// calculate and profile
problem:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs problem;func:f;0N!"No function matches"];
$[(input_file:`$ssr[problem;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"No input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;$[1<count raw_input;enlist raw_input;raw_input]];
  0N!"Result of ",problem,": ", $[10h=type r 1;r 1;string r 1];
  0N!"Time usage in milliseconds ",string r[0;0];
  0N!"Space usage in bytes ",string r[0;1]];
