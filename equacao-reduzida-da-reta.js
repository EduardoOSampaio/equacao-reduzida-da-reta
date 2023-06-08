const XA = 2;
const XB = 3;

const YA = 2;
const YB = 4;

const M = (YB - YA) / (XB - XA);

const yDoYA = M * XA;
const nDoYA = YA - yDoYA;

const yDoYB = M * XB;
const nDoYB = YB - yDoYB;

console.log({
  M,
  yDoYA,
  nDoYA,
  yDoYB,
  nDoYB,
});

console.log(`y = ${M}x + (${nDoYA})`)
