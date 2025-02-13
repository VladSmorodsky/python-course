import re


def pick_urls(text: str) -> list[str]:
    """
    Pick all urls from text.
    :param text:
    :return:
    """
    return re.findall(r"(?:https?://|www\.)[\w.\-_]+[\w/?=]+", text)


if __name__ == '__main__':
    textwrap = ("If http://test-shop.example/product?test_product you're looking for breathtaking scenery, "
                "visit www.naturephotography.com to see stunning images of landscapes. For travel tips, check "
                "out www.traveladventures.com where you can find exciting destinations and ideas. "
                "Technology enthusiasts will enjoy reading about the latest innovations at www.technewsweekly.com. "
                "For those who love to cook, www.culinarycreations.com features a variety of delicious recipes to try. "
                "If fashion is your passion, don’t forget to explore www.fashionforward.com for the newest trends. "
                "Finally, for financial advice, www.smartinvestments.com offers valuable resources https://test-shop.example "
                "to help you manage your money effectively.")
    print(pick_urls(textwrap))
