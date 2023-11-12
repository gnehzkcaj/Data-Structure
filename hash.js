function hash(input) {
    let hash = 0;
    for (let c of input) {
        hash += c.charCodeAt(0);
    }
    return hash % 1000000;
}

console.log(hash('50'))
console.log(hash('Hello World'))

let map = new Map();
map.set("hello", "world");
console.log(map.get("hello"));


class HashMap {
    constructor() {
        this.bs = [[], [], []];
    }

    bucket(key) {
        let h = murmur3(key);
        return this.bs[h % this.bs.length];
    }

    entry(bucket, key) {
        for (let e of bucket) {
            if (e.key === key) {
                return e;
            }
        }
        return null;
    }

    set(key, value) {
        let b = this.bucket(key);
        let e = this.entry(b, key);
        if (e) {
            e.value = value;
            return;
        }
        b.push({ key, value });
    }

    get(key) {
        let b = this.bucket(key);
        let e = this.entry(b, key);
        if (e) {
            return e.value;
        }
        return null;
    }
}