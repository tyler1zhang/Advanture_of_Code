// solutions
.aoc.202001part1:{prd l where (2020-l) in l:"J"$x};
.aoc.202001part2:{prd l where l in 2020-raze l+\:l:"J"$x};
.aoc.202002part1:{sum {(sum v[1][0]=v[2]) within "J"$"-" vs first v:" " vs x} each x};
.aoc.202002part2:{sum {1=sum v[1][0]=v[2] -1+"J"$"-" vs first v:" " vs x} each x};
.aoc.202003part1:{sum "#"=((1+3*c)#'x)./:n,'3*n:til c:count x};
.aoc.202003part2:{m:(1+7*c:count x)#'x; prd `long${sum "#"=y ./: x}[;m] each {((-1+z) div x){x+y}[;(x;y)]\0 0}[;;c] .' (1 1;1 3;1 5;1 7;2 1)};
.aoc.202004part1:{sum {all `byr`iyr`eyr`hgt`hcl`ecl`pid in distinct `$first each ":" vs' " " vs x} each "," vs raze " ",/:@[x;where "" ~/: x;:;","]};
.aoc.202004part2:{
  val:{[d]
    rbyr:("J"$d`byr) within 1920 2002;
    riyr:("J"$d`iyr) within 2010 2020;
    reyr:("J"$d`eyr) within 2020 2030;
    rhgt:$["cm" like -2#d`hgt;("J"$-2_d`hgt) within 150 193;("J"$-2_d`hgt) within 59 76];
    rhcl:and[(d`hcl) like "#??????";all (-6#d`hcl) in "0123456789abcdef"];
    recl:(`$d`ecl) in `amb`blu`brn`gry`grn`hzl`oth;
    rpid:(d`pid) like raze 9#enlist "[0-9]";
    all(rbyr;riyr;reyr;rhgt;rhcl;recl;rpid)};
    ds:{l:":" vs' v where not "" ~/: v:" " vs x; d:(`$l[;0])!l[;1]} each "," vs raze " ",/:@[x;where "" ~/: x;:;","];
    ds:ds where all each `byr`iyr`eyr`hgt`hcl`ecl`pid in/: key each ds;
    sum val each ds};
.aoc.202005part1:{lr:til 128; lc:til 8; .aoc.f5:{n:(count x) div 2; $[y in "FL";n # x;n _ x]};
  max {(first z .aoc.f5/ -3#x) + 8 * first y .aoc.f5/ 7#x}[;lr;lc] each x};
.aoc.202005part2:{lr:til 128; lc:til 8; .aoc.f5:{n:(count x) div 2; $[y in "FL";n # x;n _ x]};
  l:{(first z .aoc.f5/ -3#x) + 8 * first y .aoc.f5/ 7#x}[;lr;lc] each x; first -1+(prev ls) where 2=(prev ls) - ls:desc l};
.aoc.202006part1:{sum count each distinct each "," vs raze @[x;where "" ~/: x;:;","]};
.aoc.202006part2:{sum {count (inter/)v where not ""~/:v:" " vs x} each "," vs raze " ",/:@[x;where "" ~/: x;:;","]};
.aoc.202007part1:{
  k:{`$rtrim first "contain" vs ssr[x;"bags";"bag"]} each x;
  v:{v:" " vs' trim "," vs ssr[;".";""]last "contain" vs ssr[x;"bags";"bag"]; `$" " sv' 1 _' v} each x;
  .aoc.d:k!v;
  .aoc.cl:enlist `$"shiny gold bag";
  while[(count .aoc.cl) < count ncl:distinct .aoc.cl,raze {where x in/: .aoc.d} each .aoc.cl; .aoc.cl:ncl];
  -1 + count .aoc.cl};
.aoc.202007part2:{
  k:{`$rtrim first "contain" vs ssr[x;"bags";"bag"]} each x;
  v:{v:" " vs' trim "," vs ssr[;".";""]last "contain" vs ssr[x;"bags";"bag"]; ("J"$v[;0]) ,' `$" " sv' 1 _' v} each x;
  .aoc.d:k!v;
  kv:where (`$"other bag") = .aoc.d[;0][;1];
  .aoc.dv:kv!(count kv)#1;
  while[not (`$"shiny gold bag") in key .aoc.dv; .aoc.dv,:kv!{1+sum x[;0] *' .aoc.dv x[;1]} each .aoc.d kv:where all each .aoc.d[;;1] in key .aoc.dv];
  .aoc.dv[`$"shiny gold bag"]-1};
.aoc.202008part1:{
  .aoc.l:{(`$first v), "J"$last v:" " vs x} each x;
  .aoc.il:enlist 0;
  .aoc.acc:0;
  f:{i:.aoc.l x;
    if[`acc=i[0]; .aoc.acc+:i[1]; .aoc.il,:x+1];
    if[`jmp=i[0]; .aoc.il,:x+i[1]];
    if[`nop=(.aoc.l x)[0]; .aoc.il,:x+1]};
  while[not 2 in value count each group .aoc.il; f last .aoc.il];
  .aoc.acc};
.aoc.202008part2:{
  .aoc.l:{(`$first v), "J"$last v:" " vs x} each x;
  l1:{@[.aoc.l;x;{`nop,x[1]}]} each where `jmp=.aoc.l[;0];
  l2:{@[.aoc.l;x;{`jmp,x[1]}]} each where `nop=.aoc.l[;0];
  ll:l1,l2;
  ff:{l:x; .aoc.il:enlist 0; .aoc.acc:0; .aoc.flag:0b;
    f:{if[x=674;:.aoc.flag:1b];
      i:y x;
      if[`acc=i[0]; .aoc.acc+:i[1]; .aoc.il,:x+1];
      if[`jmp=i[0]; .aoc.il,:x+i[1]];
      if[`nop=i[0]; .aoc.il,:x+1]};
    while[and[not .aoc.flag;not 2 in value count each group .aoc.il]; f[;l] last .aoc.il];
    $[2 in value count each group .aoc.il;:`nto;:.aoc.acc]};
  first r where not `nto ~/: r:distinct ff each ll};
.aoc.202009part1:{l:"J"$x; f:{y[x] in raze p +/:\:p:y [x - 1 + til 25]};
  i:25; while[f[;l] i; i+:1]; l i};
.aoc.202009part2:{l:"J"$x; f:{y[x] in raze p +/:\:p:y [x - 1 + til 25]}; i:25; while [f[;l] i; i+:1];
  p:{y[z] = sum each y @ (til z - x) +\: til x}[;l;i]; 
  n:3; while[not any p n; n+:1];
  rg:nl where l[i] = sum each l @ nl:(til i - n) +\: til n;
  sum (min;max) @\: l raze rg};
.aoc.202010part1:{prd value count each group 1, 3^(next l) - l:asc "J"$x};
.aoc.202010part2:{d:count each group -1 _ (next p) - p:-1, where 3 = 3^(next l) - l:0,asc "J"$x; prd raze (d 5 4 3) #' 7 4 2};
.aoc.202011part1:{.aoc.s:x; .aoc.p:x; .aoc.c:(count x)#enlist (count first x)#" ";
  f:{s:.aoc.s . x;
    n:{x[y][z]}[.aoc.s;;] .' (x +/: raze a ,\:/: a:-1 0 1) except enlist x;
    if[and["L" = s;not "#" in n]; .[`.aoc.c;x;:;"#"]];
    if[and["#" = s;4 <= sum "#" = n]; .[`.aoc.c;x;:;"L"]]};
  while[not .aoc.c ~ .aoc.p; .aoc.p:.aoc.s; f each raze (til count x) ,/:\: (til count first x); .aoc.s:.aoc.c];
  sum "#" = raze .aoc.c};
.aoc.202011part2:{.aoc.s:x; .aoc.p:x; .aoc.c:(count x)#enlist (count first x)#" ";
  .aoc.row:count x; .aoc.col:count first x;
  f:{i:x[0]; j:x[1];
    l1:i ,' lr:j + 1 _ til .aoc.col - j;
    l2:i ,' ll:reverse til j;
    l3:(ld:i + 1 _ til .aoc.row - i) ,' j;
    l4:(lu:reverse til i) ,' j;
    df:{(,') . (min count each (x;y))#'(x;y)};
    l5:df[ld;lr];
    l6:df[lu;lr];
    l7:df[ld;ll];
    l8:df[lu;ll];
    st:.aoc.s . x;
    n:raze first each sl @' where each any "L#" =\: sl:.aoc.s ./:/: (l1;l2;l3;l4;l5;l6;l7;l8);
    if[and["L" = st;not "#" in n]; .[`.aoc.c;x;:;"#"]];
    if[count n; if[and["#" = st;5 <= sum "#" = n]; .[`.aoc.c;x;:;"L"]]]};
  while[not .aoc.c ~ .aoc.p; .aoc.p:.aoc.s; f each raze (til count x) ,/:\: (til count first x); .aoc.s:.aoc.c];
  sum "#" = raze .aoc.c};
.aoc.202012part1:{
  .aoc.d:0 1 2 3!`E`S`W`N;
  .aoc.dc:-3 -2 -1 0 1 2 3 4 5 6!`S`W`N`E`S`W`N`E`S`W;
  .aoc.p:0 0; 
  .aoc.f:`E;
  g:{if[x[0] in `E`S`W`N; .aoc.p+:x[1] * (`E`S`W`N!(1 0;0 -1;-1 0;0 1))x[0]];
    if[x[0] in `L`R; d:x[1] div 90; .aoc.f:.aoc.dc (.aoc.d?.aoc.f) + ((`L`R!(neg;eval))x[0]) @ d];
    if[x[0]=`F; .aoc.p+:x[1] * (`E`S`W`N!(1 0;0 -1;-1 0;0 1)).aoc.f]};
  g each {(`$first x;"J"$1 _ x)} each x;
  sum abs .aoc.p};
.aoc.202012part2:{
  .aoc.wp:10 1; 
  .aoc.sp:0 0;
  g:{if[x[0] in `E`S`W`N; .aoc.wp+:x[1] * (`E`S`W`N!(1 0;0 -1;-1 0;0 1))x[0]];
    if[x[0]in`L`R; d:((`L`R!(neg;eval))x[0]) @ x[1] div 90; 
      if[1 = abs d;.aoc.wp:@[reverse .aoc.wp;(-1 1!0 1)d;neg]];
      if[2 = abs d;.aoc.wp:neg .aoc.wp];
      if[3 = abs d;.aoc.wp:@[reverse .aoc.wp;(-3 3!1 0)d;neg]]];
    if[x[0]=`F; .aoc.sp+:.aoc.wp * x[1]]};
  g each {(`$first x;"J"$1 _ x)} each x;
  sum abs .aoc.sp};


// calculate and profile
problem:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs problem;func:f;0N!"No function matches"];
$[(input_file:`$ssr[problem;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"No input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;$[1<count raw_input;enlist raw_input;raw_input]];
  0N!"Result of ",problem,": ", $[10h=type r 1;r 1;string r 1];
  0N!"Time usage in milliseconds ",string r[0;0];
  0N!"Space usage in bytes ",string r[0;1]];
