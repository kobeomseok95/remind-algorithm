def solution(enroll, referral, seller, amount):
    org_chart = {enroll[i]: referral[i] for i in range(len(enroll))}
    benefits = calculate_benefits(org_chart, enroll, seller, amount)
    return [benefits[emp] for emp in enroll]


def calculate_benefits(org_chart, enroll, sellers, amounts):
    benefits = {name: 0 for name in enroll}
    benefits["-"] = 0
    for seller, amount in zip(sellers, amounts):
        total_amount = amount * 100
        seller_name = seller
        while seller_name in org_chart:
            referral_amount = total_amount // 10
            my_amount = total_amount - referral_amount
            benefits[seller_name] += my_amount
            total_amount = referral_amount
            seller_name = org_chart[seller_name]
            if referral_amount == 0:
                break
    return benefits
