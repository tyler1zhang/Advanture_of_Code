// util functions
.aoc.AND:{0b sv (and/) 0b vs' x,y};
.aoc.OR:{0b sv (or/) 0b vs' x,y};
.aoc.NOT:{(`long$2 xexp 16) + 0b sv not 0b vs x};
.aoc.LSHIFT:{0b sv next/[y;0b vs x]};
.aoc.RSHIFT:{0b sv prev/[y;0b vs x]};
.aoc.SELF:{x};
.aoc.perm:{{raze x{x,/:y except x}\:y}[;y]/[x-1;y]};
.aoc.lookAndSay:{[n] c:1+(n=flip 1_next\[2;n])?\:0b; raze flip (c;n) @\: m:where not 1<prev c};
.aoc.comb:{{raze x{x,/:y where y>max x}\:y}[;y]/[x-1;y]};
.aoc.divisors:{distinct l,x div l:t where 0=x mod t:1+til floor sqrt x};


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
.aoc.201507part1: {cs:" " vs' x;
                   inputs:{x where not x in\: ("AND";"OR";"NOT";"LSHIFT";"RSHIFT")} each -2_'cs;
                   gates:{first `$x where x in\: ("AND";"OR";"NOT";"LSHIFT";"RSHIFT")} each -2_'cs;
                   outputs:`$last each cs;
                   iFunc:{@[;where not all each x in .Q.a;"J"$]@[x;where all each x in .Q.a;`$]};
                   cTab:update iFunc each input from flip `output`input`gate!(outputs;inputs;gates);
                   cTab:update gate:`SELF from cTab where gate=`;
                   eFunc:{v:$[-7h in t:type each i:x[`input];@[i;where -11h=t;@[value;;{::}]];@[value;;{::}] each i where -11h=t];
                          x[`output] set .[.aoc[x`gate];v;{::}]};
                   while[null @[value;`a;{::}];eFunc each cTab];a};
.aoc.201507part2: {cs:" " vs' x;
                   inputs:{x where not x in\: ("AND";"OR";"NOT";"LSHIFT";"RSHIFT")} each -2_'cs;
                   gates:{first `$x where x in\: ("AND";"OR";"NOT";"LSHIFT";"RSHIFT")} each -2_'cs;
                   outputs:`$last each cs;
                   iFunc:{@[;where not all each x in .Q.a;"J"$]@[x;where all each x in .Q.a;`$]};
                   cTab:update iFunc each input from flip `output`input`gate!(outputs;inputs;gates);
                   cTab:update gate:`SELF from cTab where gate=`;
                   cTab:update input:enlist enlist 16076 from cTab where output=`b;
                   eFunc:{v:$[-7h in t:type each i:x[`input];@[i;where -11h=t;@[value;;{::}]];@[value;;{::}] each i where -11h=t];
                          x[`output] set .[.aoc[x`gate];v;{::}]};
                   while[null @[value;`a;{::}];eFunc each cTab];a};
.aoc.201508part1: {cb:{count ss[-1 _ 1 _ x;"\\\\"]};
                   cs:{count ss[-1 _ 1 _ x;"\\\""]};
                   cx:{3 * count (except/) 0 1 + ss[-1 _ 1 _ x;] each ("\\x";"\\\\")};
                   sum {[x;cb;cs;cx] 2 + sum (cb;cs;cx) @\: x}[;cb;cs;cx] each x};
.aoc.201508part2: {sum {2 + sum any ("\"";"\\") =\: x} each x};
.aoc.201509part1: {d:(`$l[;0 2],l[;2 0])!"J"${x,x}(l:" " vs' x)[;4];
                   rl:.aoc.perm[count cl;cl:distinct `$raze l[;0 2]];
                   min {sum y x,'next x}[;d] each rl};
.aoc.201509part2: {d:(`$l[;0 2],l[;2 0])!"J"${x,x}(l:" " vs' x)[;4];
                   rl:.aoc.perm[count cl;cl:distinct `$raze l[;0 2]];
                   max {sum y x,'next x}[;d] each rl};
.aoc.201510part1: {count .aoc.lookAndSay/ [40;"J"$'raze x]};
.aoc.201510part2: {count .aoc.lookAndSay/ [50;"J"$'raze x]};
.aoc.201511part1: {p:$[10h=type x;x;raze x];
                   .aoc.d11:(.Q.a!til 26);
                   c1:{any min 1 = 1 _ deltas (next\)[2;.aoc.d11 x]};
                   c2:{all not "iol" in x};
                   c3:{and[4<=count distinct p,1+p:where b; 2<=sum b:x=next x]};
                   .aoc.increment11:{$[not null n:.aoc.d11 ? 1+.aoc.d11 x[y];@[x;y;:;n];[x:@[x;y;:;"a"];.z.s[x;y-1]]]};
                   while[not all (c1;c2;c3) @\: p; p:.aoc.increment11[p;7]];p};
.aoc.201511part2: {.aoc.201511part1 .aoc.increment11[;7].aoc.201511part1 x};
.aoc.201512part1: {sum l where -9h=type each l:(raze/){$[9h=abs type x;x;10h=type x;`$x;99h=type x;.z.s each value x;.z.s each x]} .j.k raze x};
.aoc.201512part2: {sum l where 9h=abs type each l:(raze/){$[9h=abs type x;x;10h=type x;`$x;99h=type x;$[any "red" ~/: x;();.z.s each value x];.z.s each x]} .j.k raze x};
.aoc.201513part1: {d:(`$l[;0 10])!"J"$((("gain";"lose")!"+-") l[;2]),'(l:" " vs' -1_'raw_input)[;3];
                   sl:.aoc.perm[count pl;pl:gl except hg:first gl:distinct `$raze l[;0 10]];
                   max {sum y {x, reverse each x} x,'1 rotate x}[;d] each hg,/:sl};
.aoc.201513part2: {d:(`$l[;0 10])!"J"$((("gain";"lose")!"+-") l[;2]),'(l:" " vs' -1_'raw_input)[;3];
                   nd:({x, reverse each x} `Sui,'gl)!(2*count gl:distinct `$raze l[;0 10])#0;
                   nd:d,nd;
                   sl:.aoc.perm[count gl;gl];
                   max {sum y {x, reverse each x} x,'1 rotate x}[;nd] each `Sui,/:sl};
.aoc.201514part1: {max {(x*y*2503 div (y+z))+$[y<=m:2503 mod (y+z);x*y;x*m]} .' n @' where each not null n:"J"$" " vs' x};
.aoc.201514part2: {max sum each m =\: max m:({[x;y;z;t](x*y*t div (y+z))+$[y<=m:t mod (y+z);x*y;x*m]} .' n @' where each not null n:"J"$" " vs' x) @/:\: 1+til 2503};
.aoc.201515part1: {f:"J"$-1_''(" " vs' x)[;2 4 6 8];
                   c:{x,100 - sum x} each raze/[2;] {$[3h=count x;x;.z.s each x ,/: til 101 - sum x]} each til 101;
                   max {prd @[s;where 0>s:sum x * y;:;0]}[f;] each c};
.aoc.201515part2: {f:"J"$-1_''(" " vs' x)[;2 4 6 8];
                   e:"J"$(" " vs' x)[;10];
                   c:c where 500=sum each e */: c:{x,100 - sum x} each raze/[2;] {$[3h=count x;x;.z.s each x ,/: til 101 - sum x]} each til 101;
                   max {prd @[s;where 0>s:sum x * y;:;0]}[f;] each c};
.aoc.201516part1: {d:`children`cats`samoyeds`pomeranians`akitas`vizslas`goldfish`trees`cars`perfumes!3 7 2 3 0 0 5 3 2 1;
                   first value first as where {all (value x)=y key x}[;d] each 1_'as:{(`$x[0 2 4 6])!"J"$x[1 3 5 7]} each " " vs' {ssr[;",";""]ssr[x;":";""]} each x};
.aoc.201516part2: {d:`children`cats`samoyeds`pomeranians`akitas`vizslas`goldfish`trees`cars`perfumes!({x=3};{x>7};{x=2};{x<3};{x=0};{x=0};{x<5};{x>3};{x=2};{x=1});
                   first value first as where {all (y key x) @' value x}[;d] each 1_'as:{(`$x[0 2 4 6])!"J"$x[1 3 5 7]} each " " vs' {ssr[;",";""]ssr[x;":";""]} each x};
.aoc.201517part1: {l:desc "J"$x; .aoc.counter17:0;
                   {[n;i;l].aoc.counter17+:sum 150=n+l[where i<til count l];if[sum b:150>m:n+l[j:where i<til count l];.z.s[;;l] .' flip(m;j) @\: where b]}[;;l] .' l,'til count l;
                   .aoc.counter17};
.aoc.201517part2: {l:desc "J"$x; m:{while[150>sum x#y;x+:1];x}[1;l]; sum 150=sum each l .aoc.comb[m;til count l]};
.aoc.201518part1: {.aoc.n:m:("#."!10b) x;
                   {{[m;i;j] if[m[i;j];if[not (sum {z[x;y]}[;;m] .' except[(cross/)o+\:(-1 0 1);enlist o:(i;j)]) in 2 3;.aoc.n[i;j]:0b]];
                             if[not m[i;j];if[(sum {z[x;y]}[;;m] .' except[(cross/)o+\:(-1 0 1);enlist o:(i;j)]) = 3;.aoc.n[i;j]:1b]];}
                    [x;;] .' {x cross x} til count x; .aoc.n}/[100;m]; sum sum each .aoc.n};
.aoc.201518part2: {m:("#."!10b) x; m[0;0]:m[0;99]:m[99;0]:m[99;99]:1b; .aoc.n:m;
                   {{[m;i;j] if[m[i;j];if[not (sum {z[x;y]}[;;m] .' except[(cross/)o+\:(-1 0 1);enlist o:(i;j)]) in 2 3;.aoc.n[i;j]:0b]];
                             if[not m[i;j];if[(sum {z[x;y]}[;;m] .' except[(cross/)o+\:(-1 0 1);enlist o:(i;j)]) = 3;.aoc.n[i;j]:1b]];}
                    [x;;] .' ({x cross x} til count x) except (0 0;0 99;99 0;99 99);.aoc.n}/[100;m]; sum sum each .aoc.n};
.aoc.201519part1: {count distinct raze {{[i;j;r;s] (i#s),r,j _ s}[;;x[1];y] .' p ,' (p:ss[y;x[0]])+count x[0]}[;last x] each (" " vs' -2_x)[;0 2]};
.aoc.201520part1: {i:1; while[("J"$raze x) > sum 10*.aoc.divisors i;i+:1]; i};
.aoc.201520part2: {i:1; while[("J"$raze x) > sum 11*d where i<=50*(d:.aoc.divisors i);i+:1]; i};
.aoc.201521part1: {`bp`bd`ba set' "J"$last each " " vs' x; pp:100;
                   weapons:([]name:`dagger`shortsword`warhammer`longsword`greataxe;cost:8 10 25 40 74;damage:4 5 6 7 8;armor:0 0 0 0 0);
                   armor:([]name:`leather`chainmail`splintmail`bandedmail`platemail;cost:13 31 53 75 102;damage:0 0 0 0 0;armor:1 2 3 4 5);
                   rings:([]name:`damage1`damage2`damage3`defense1`defense2`defense3;cost:25 50 100 20 40 80;damage:1 2 3 0 0 0;armor:0 0 0 1 2 3);
                   es:(cross/)(exec name from weapons; `,exec name from armor; `,r,.aoc.comb[2;r:exec name from rings]);
                   wf:{[bp;bd;ba;pp;pd;pa] (<=/) ceiling each (bp % max(pd - ba;1); pp % max(bd - pa;1))}[bp;bd;ba;pp;;];
                   wes:es where wf .' value each {exec sum damage, sum armor from y where name in x}[;raze (weapons;armor;rings)] each es;
                   min {exec sum cost from y where name in x}[;raze (weapons;armor;rings)] each wes};
.aoc.201521part2: {`bp`bd`ba set' "J"$last each " " vs' x; pp:100;
                   weapons:([]name:`dagger`shortsword`warhammer`longsword`greataxe;cost:8 10 25 40 74;damage:4 5 6 7 8;armor:0 0 0 0 0);
                   armor:([]name:`leather`chainmail`splintmail`bandedmail`platemail;cost:13 31 53 75 102;damage:0 0 0 0 0;armor:1 2 3 4 5);
                   rings:([]name:`damage1`damage2`damage3`defense1`defense2`defense3;cost:25 50 100 20 40 80;damage:1 2 3 0 0 0;armor:0 0 0 1 2 3);
                   es:(cross/)(exec name from weapons; `,exec name from armor; `,r,.aoc.comb[2;r:exec name from rings]);
                   lf:{[bp;bd;ba;pp;pd;pa] (>/) ceiling each (bp % max(pd - ba;1); pp % max(bd - pa;1))}[bp;bd;ba;pp;;];
                   les:es where lf .' value each {exec sum damage, sum armor from y where name in x}[;raze (weapons;armor;rings)] each es;
                   max {exec sum cost from y where name in x}[;raze (weapons;armor;rings)] each les};


// calculate and profile
problem:raze (.Q.opt .z.x) `problem;
$[100h=type f:.aoc`$raze "_" vs problem;func:f;0N!"No function matches"];
$[(input_file:`$ssr[problem;"part?";"input.txt"]) in key `:.;raw_input:read0 input_file;0N!"No input file matchs"];
if[all `func`raw_input in key `.;
  r:.Q.ts[func;$[1<count raw_input;enlist raw_input;raw_input]];
  0N!"Result of ",problem,": ", $[10h=type r 1;r 1;string r 1];
  0N!"Time usage in milliseconds ",string r[0;0];
  0N!"Space usage in bytes ",string r[0;1]];
