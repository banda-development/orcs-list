
def main():
    with open("index.html", "r", encoding="utf-8") as index_file:
        data = index_file.read()
        for i in range(1, 64):
            build_data = data.replace("data_0.csv", f"data_{i}.csv")
            build_data = build_data.replace("/1.html", f"/{i+1}.html")
            build_data = build_data.replace("/first.html",f"/{i-1}.html")
            with open(f"{i}.html", "w", encoding="utf-8") as build_file:
                build_file.write(build_data)




if __name__ == "__main__":
    main()