// Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

// For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

// FUNDAMENTALSMATHEMATICSa

//MY SOLUTIONS

// let quarterOf = (month) => {
//     return Math.ceil(month/3)
// };

//Alternative
let quarterOf = (month) => {
    if(month<4){
      return 1;
    } else if(3<month && month<7){
      return 2;
    } else if(6<month && month<10){
      return 3;
    }
    return 4;
};
