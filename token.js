const secret = "87ADB446E4B5727AD6F47B8DFB7C6";
class Token {
  constructor(secret) {
    this.secret = secret;
  }
  getSum() {
    let dict = {};
    for (let i = 0; i < this.secret.length; i++) {
      dict[this.secret[i]] = i;
    }
    let sum = Object.values(dict).reduce((a, b) => a + b, 0);
    return sum;
  }

  getNow() {
    const now = new Date();
    const month = now.getMonth() + 1;
    const day = now.getDate();
    const hour = now.getHours();
    const minute = now.getMinutes();
    const second = now.getSeconds()-1;
    return month + day + hour + minute + second;
  }

  getToken() {
    return this.getSum() * this.getNow();
  }
}

const token = new Token(secret);
console.log(token.getToken(), "token");
