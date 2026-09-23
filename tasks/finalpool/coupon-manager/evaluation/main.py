from src.coupon_manager import CouponManager


def evaluate():
    manager = CouponManager()
    result = manager.run()
    return result


if __name__ == "__main__":
    print(evaluate())
