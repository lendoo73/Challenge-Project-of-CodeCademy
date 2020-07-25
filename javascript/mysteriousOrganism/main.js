// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G']
  return dnaBases[Math.floor(Math.random() * 4)] 
}

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = []
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase())
  }
  return newStrand
}

// 3-4:
const randNum = (min, max) => Math.floor(Math.random() * (max + 1 - min)) + min;

const getPercentage = (a, b, fix = 0) => (a / b * 100).toFixed(fix);

const pAequorFactory = (num, baseDNA) => {
  const dnaSecv = {
    specimenNum: num,
    dna: baseDNA,
    mutate: () => {
      const i = randNum(0, baseDNA.length);
      let randomBase;
      do {
        randomBase = returnRandBase();
      } while (randomBase === baseDNA[i]);
      baseDNA[i] = randomBase;
      return baseDNA;
    },
    compareDNA: (pAequor, num = false) => {
      const firstDNA = pAequor.dna;
      let counter = 0;
      firstDNA.forEach((elem, i) => {
        if (firstDNA[i] === dnaSecv.dna[i]) counter ++;
      });
      const percent = getPercentage(counter, firstDNA.length);
      if (num) return percent;
      console.log(`specimen #${dnaSecv.specimenNum} and specimen #${pAequor.specimenNum} have ${percent}% DNA in common`);
    },
    willLikelySurvive: () => {
      const dna = dnaSecv.dna;
      let counter = 0;
      dna.forEach(elem => {
        if (elem === "C" || elem === "G") counter ++;
      });
      return getPercentage(counter,dna.length) >= 60;
    }, // 9:
    complementStrand: () => dnaSecv.dna.map(base => {
      if (base === "A") return "T";
      if (base === "T") return "A";
      if (base === "C") return "G";
      if (base === "G") return "C";
    })
  };
  return  dnaSecv;
};

const myDNA = pAequorFactory(1, mockUpStrand());
const nextDNA = pAequorFactory(2, mockUpStrand());
//console.log(myDNA);
//console.log(nextDNA);
nextDNA.compareDNA(myDNA);
//myDNA.mutate();
//console.log(myDNA);
console.log(myDNA.willLikelySurvive());
console.log(nextDNA.willLikelySurvive());

// 7:
const surviveSample = [];

do {
  const sample = pAequorFactory(surviveSample.length + 1, mockUpStrand());
  if (sample.willLikelySurvive()) surviveSample.push(sample);
} while (surviveSample.length < 30);

//console.log(surviveSample.map(sample => sample.willLikelySurvive()));
//console.log(myDNA.dna);

//console.log(myDNA.complementStrand());

// 9: most related instances:
let instance1 = surviveSample[0],
  instance2 = surviveSample[1],
  highest = 0;

surviveSample.forEach((a, ai) => {
  surviveSample.forEach((b, bi) => {
    if (ai !== bi) {
      const related = + a.compareDNA(b, true);
      if  (related > highest) {
        instance1 = a;
        instance2 = b;
        highest = related;
      } 
    }
  });
});

console.log(`sample #${instance1.specimenNum} and sample #${instance2.specimenNum} have ${highest}% DNA in common`);
