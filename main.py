import hashlib
from random import randint

# assuming that payment is worth the value of one coin
def hash(x, y):
    input = x + y
    hex_out = hashlib.md5(input.encode("utf-8")).hexdigest()
    return hex_out[0:8]


def rand_num():
    a = str(randint(0, (2**32) - 1))
    pad_size = 10 - len(a)
    out = pad_size * "0" + a
    return out


class Bank:
    list_of_acc = [["alice", 96.32, 82028], ["bob", 136000.00, 93737]]

    def __init__(self, d, e, n):
        self._d = d
        self.e = e
        self.n = n

    def find_customer(self, customer_name):
        names = [elem[0] for elem in self.list_of_acc]
        index_of_acc = names.index(customer_name.lower())
        return (
            self.list_of_acc[index_of_acc][0],
            str(self.list_of_acc[index_of_acc][1]),
            str(self.list_of_acc[index_of_acc][2]),
        )

    def open_chunks(self, customer, k=10, k2=10):
        # generate list of random chunks to open
        index_options = list(range(0, k + k2))
        chunk_index = []
        for _ in range(k2):
            index = randint(0, len(index_options) - 1)
            chunk_index.append(index_options.pop(index))
        chunk_index.sort()

        # rename for better readability:
        # remaining_chunks represents the chunks that remain blinded and unseen by bank
        remaining_chunks = index_options

        # tells customer to open chunks
        customer.expose_chunks(chunk_index)
        with open("bank_verify.txt", "r") as data_file, open(
            "to_sign.txt"
        ) as chunks_file:
            bill_num = chunks_file.readline()

            for i in chunk_index:
                data_line = data_file.readlines()[i: i+1][0]
                h = customer.acc + bill_num
                r, a, c, d = data_line.split(",")
                hxor = str(int(a) ^ int(h))
                x = str(int(hash(a, c), base=16))
                y = str(int(hash(hxor, d), base=16))
                chunk_tmp = int(hash(x,y), base=16)

                blinding_factor = pow(int(r), int(self.e))
                blinded_chunk_tmp = chunk_tmp * blinding_factor

                blinded_chunk = chunks_file.readlines()[i: i+1][0]

                # checks whether bank recreation is equal to value submitted by alice
                if blinded_chunk != blinded_chunk_tmp:
                    raise ValueError("Alice submitted incorrect value")
            for i in remaining_chunks:
                chunks_lines = chunks_file.readlines()[i + 1 : i + 2]
                chunk = chunks_lines[0]
                signed_chunk = (int(chunk) ** d) % n

class customer:
    recent_chunks = []

    def __init__(self, bank, name):
        # returns data known to bank about customer
        self.name, self.value, self.acc = bank.find_customer(name)
        # makes bank known to user
        self.bank = bank

    def generate_chunks(self, k=10, k2=10):
        bill_num = str(randint(10000, 99999))

        with open("to_sign.txt", "a") as file:
            file.write(str(bill_num) + "\n")

        h = self.acc + bill_num

        for i in range(k + k2):
            # chunks
            a = rand_num()
            c = rand_num()
            d = rand_num()
            r = randint(2, 25)
            hxor = str(int(a) ^ int(h))
            x = str(int(hash(a, c), base=16))
            y = str(int(hash(hxor, d), base=16))
            blinding_factor = pow(r, self.bank.e)

            chunk_val = int(hash(x, y), base=16)
            blind_chunk = chunk_val * blinding_factor

            self.recent_chunks.append([blind_chunk, r, a, c, d])

            print(r,a,c,d,"hxor",hxor,"x",x,"y",y,"blind", blinding_factor, "chunkval", chunk_val, "blind_chunk", blind_chunk)

            with open("to_sign.txt", "a") as file:
                file.write(str(blind_chunk) + "\n")

    def expose_chunks(self, index):
        with open("bank_verify.txt", "a") as file:
            for i in index:
                chunk_info = self.recent_chunks[i]
                file.write(
                    str(chunk_info[1])
                    + ","
                    + str(chunk_info[2])
                    + ","
                    + str(chunk_info[3])
                    + ","
                    + str(chunk_info[4])
                )
                file.write("\n")


# p = 103141
# q = 197261
# phin = 20345396400
d = 4695091477
e = 13
n = 20_345_696_801
bank = Bank(d, e, n)
alice = customer(bank, "alice")
alice.generate_chunks()
bank.open_chunks(alice)
