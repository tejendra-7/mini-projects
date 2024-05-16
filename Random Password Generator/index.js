function generatePassword(length , includeLowercase , includeUppercase , includeNumbers , includeSymbols) {
    const lowercase = 'abcdefghijklmnopqrstuvwxyz';
    const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numbers = '0123456789';
    const symbols = '!@#$%^&*()_+{}:"<>?|[];\',./`~';

    let allowedChars = '';
    let password = '';

    allowedChars += (includeLowercase) ? lowercase : '';
    allowedChars += (includeUppercase) ? uppercase : '';
    allowedChars += (includeNumbers) ? numbers : '';
    allowedChars += (includeSymbols) ? symbols : '';


    if (allowedChars.length === 0) {
        return `(At least 1 set of characters needs to be selected)`;
    }
    if (length <= 0) {
        return `Password length must be at least 1`;
    }

    for(let i = 0; i<length; i++){
        const randomIndex = Math.floor(Math.random() * allowedChars.length);
        password += allowedChars[randomIndex];
    }

    return password;
}

const passwordlength = 12;
const includeLowercase = true;
const includeUppercase = true; 
const includeNumbers = true;
const includeSymbols = true;


let password = generatePassword(12, true, true, true, true);

console.log("Password: ", password);