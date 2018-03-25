from SynThai import SynThai


synthai = SynThai('SynThai/0063-0.0412.hdf5', 60)

text = "ข้าวมันไก่ราคาเท่าไหร่"

token = synthai.tokenize(text)

print(token)