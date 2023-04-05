# 100$ for 100 chickens
"""
公鸡五元，母鸡三元，小鸡三个一元
"""

def main():
    for gongji in range(0, 101):
        for muji in range(0, 101):
            for xiaoji in range(0, 101, 3):
                if gongji * 5 + muji * 3 + xiaoji / 3 == 100 and gongji + muji + xiaoji == 100:
                    print("公鸡%d只，母鸡%d只，小鸡%d只" % (gongji, muji, xiaoji))


if __name__ == "__main__":
    main()
