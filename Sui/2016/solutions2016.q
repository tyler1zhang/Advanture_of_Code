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


// calculate and profile
problem:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs problem;func:f;0N!"No function matches"];
$[(input_file:`$ssr[problem;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"No input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;$[1<count raw_input;enlist raw_input;raw_input]];
  0N!"Result of ",problem,": ", $[10h=type r 1;r 1;string r 1];
  0N!"Time usage in milliseconds ",string r[0;0];
  0N!"Space usage in bytes ",string r[0;1]];
