"use strict";
// All valid credit card numbers
const valid1 = [4, 5, 3, 9, 6, 7, 7, 9, 0, 8, 0, 1, 6, 8, 0, 8];
const valid2 = [5, 5, 3, 5, 7, 6, 6, 7, 6, 8, 7, 5, 1, 4, 3, 9];
const valid3 = [3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6];
const valid4 = [6, 0, 1, 1, 1, 4, 4, 3, 4, 0, 6, 8, 2, 9, 0, 5];
const valid5 = [4, 5, 3, 9, 4, 0, 4, 9, 6, 7, 8, 6, 9, 6, 6, 6];

// All invalid credit card numbers
const invalid1 = [4, 5, 3, 2, 7, 7, 8, 7, 7, 1, 0, 9, 1, 7, 9, 5];
const invalid2 = [5, 7, 9, 5, 5, 9, 3, 3, 9, 2, 1, 3, 4, 6, 4, 3];
const invalid3 = [3, 7, 5, 7, 9, 6, 0, 8, 4, 4, 5, 9, 9, 1, 4];
const invalid4 = [6, 0, 1, 1, 1, 2, 7, 9, 6, 1, 7, 7, 7, 9, 3, 5];
const invalid5 = [5, 3, 8, 2, 0, 1, 9, 7, 7, 2, 8, 8, 3, 8, 5, 4];

// Can be either valid or invalid
const mystery1 = [3, 4, 4, 8, 0, 1, 9, 6, 8, 3, 0, 5, 4, 1, 4];
const mystery2 = [5, 4, 6, 6, 1, 0, 0, 8, 6, 1, 6, 2, 0, 2, 3, 9];
const mystery3 = [6, 0, 1, 1, 3, 7, 7, 0, 2, 0, 9, 6, 2, 6, 5, 6, 2, 0, 3];
const mystery4 = [4, 9, 2, 9, 8, 7, 7, 1, 6, 9, 2, 1, 7, 0, 9, 3];
const mystery5 = [4, 9, 1, 3, 5, 4, 0, 4, 6, 3, 0, 7, 2, 5, 2, 3];

// An array of all the arrays above
const batch = [valid1, valid2, valid3, valid4, valid5, invalid1, invalid2, invalid3, invalid4, invalid5, mystery1, mystery2, mystery3, mystery4, mystery5];


// Add your functions below:
const getArrayOfNums = string => {
  return string.split("").map((num, i, arr)  => arr[i] = + arr[i]);
};

const doubleNum = num => {
  const result = num * 2;
  return result > 9 ? result - 9 : result;
};
const validateCred = arr => {
  let sum = 0;
  for (
    let i = arr.length - 1, step = true; 
    i >= 0; 
    i --) {
    if (step) {
      step = false;
      sum += arr[i];
    } else {
      step = true;
      sum += doubleNum(arr[i]);
    }
  }
  return !(sum % 10);
};

const findInvalidCards = nestedArr => {
  const invalidCards = [];
  nestedArr.forEach(card => {
    if (!(validateCred(card))) invalidCards.push(card);
  });
  return invalidCards;
};

// param: nested array
const idInvalidCardCompanies = invalidCards => {
  const companies = {
    "3": "American Express",
    "4": "Visa",
    "5": "Mastercard",
    "6": "Discovery"
  }, result = [];
  invalidCards.forEach(card => {
    const key = card[0];
    let company = "Company not found";
    if (key in companies) {
      company = companies[key];
    }
    if (!(result.includes(company))) {
        result.push(company);
    }
  });
  return result;
};

console.log(validateCred(valid1));
console.log(validateCred(valid2));
console.log(validateCred(valid3));
console.log(validateCred(valid4));
console.log(validateCred(valid5));
console.log(validateCred(invalid1));
console.log(validateCred(invalid2));
console.log(validateCred(invalid3));
console.log(validateCred(invalid4));
console.log(validateCred(invalid5));
const invalidCards = findInvalidCards(batch);
//console.log(invalidCards);
const companies = idInvalidCardCompanies(invalidCards);
console.log(companies);

// 7:
  // visa cards:
const visa1 = getArrayOfNums("4716557763192578");
const visa2 = getArrayOfNums("4539622046649250");
const visa3 = getArrayOfNums("4929293539665535075");

const visaCards = [visa1, visa2, visa3];

const invalidVisaCards = findInvalidCards(visaCards);
console.log(invalidVisaCards);

  // master cards:
const masterCard1 = getArrayOfNums("5399389696494405");
const masterCard2 = getArrayOfNums("5173822087061567");
const masterCard3 = getArrayOfNums("5196927082093599");
const masterCards = [masterCard1, masterCard2, masterCard3];
const invalidMasterCards = findInvalidCards(masterCards);
console.log(invalidVisaCards);
