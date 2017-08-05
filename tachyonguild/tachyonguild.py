import gw2api.v2


def main():
    response = gw2api.v2.achievements.get_daily()
    print(response)
    return 0


if __name__ == '__main__':
    main()
