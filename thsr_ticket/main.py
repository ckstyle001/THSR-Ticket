import sys
import time
import argparse
sys.path.append("./")

from thsr_ticket.remote.endpoint_client import EndpointClient
from thsr_ticket.model.json.v1.train import Train
from thsr_ticket.controller.booking_flow import BookingFlow


def main():
    parser = argparse.ArgumentParser(description='這是一個帶參數的 Python 程式示例')

    # 添加參數
    parser.add_argument('-d','--date', type=str, help='搭乘日期(YYYY-MM-DD)')
    parser.add_argument('-r','--record', type=int, help='使用紀錄索引編號')
    parser.add_argument('--verbose', action='store_true', help='啟用詳細模式')
    
    # 解析命令行參數
    args = parser.parse_args()
    
    # 使用參數
    if args.verbose:
        print("啟用了詳細模式")
    
    if args.date:
        print(f"搭乘日期：{args.date}")
    
    if args.record:
        print(f"使用紀錄索引編號：{args.record}")

    rc = False
    while not rc:
        flow = BookingFlow()
        rc = flow.run(args.date, args.record)
        # time.sleep(3)


if __name__ == "__main__":
    #client = EndpointClient()
    #resp = client.get_trains_by_date("2020-01-25")
    #train = Train().from_json(resp[0])

    main()
