import winreg
import subprocess


# 设置代理服务器
def set_proxy(proxy):
    try:
        # 打开 Internet 设置项
        internet_settings = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                           r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                           0, winreg.KEY_ALL_ACCESS)

        # 开启代理
        winreg.SetValueEx(internet_settings, 'ProxyEnable', 0, winreg.REG_DWORD, 1)

        # 设置代理服务器地址
        winreg.SetValueEx(internet_settings, 'ProxyServer', 0, winreg.REG_SZ, proxy)

        # 刷新设置
        subprocess.call(r'"%s" -Command "(New-Object -ComObject InternetExplorer.Application).Navigate2(%s)"'
                        % (r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', r'"https://www.google.com/"'))

        return True

    except Exception as e:
        print(e)
        return False


# 取消代理服务器设置
def unset_proxy():
    try:
        # 打开 Internet 设置项
        internet_settings = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                           r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                           0, winreg.KEY_ALL_ACCESS)

        # 关闭代理
        winreg.SetValueEx(internet_settings, 'ProxyEnable', 0, winreg.REG_DWORD, 0)

        # 刷新设置
        subprocess.call(r'"%s" -Command "(New-Object -ComObject InternetExplorer.Application).Navigate2(%s)"'
                        % (r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', r'"https://www.google.com/"'))

        return True

    except Exception as e:
        print(e)
        return False


# 示例用法
proxy = "http://127.0.0.1:8888"  # 假设代理服务器地址为 127.0.0.1:8888

if set_proxy(proxy):
    print("代理服务器设置成功")
else:
    print("代理服务器设置失败")

# 需要代理的网络请求代码放在这里

if unset_proxy():
    print("代理服务器取消成功")
else:
    print("代理服务器取消失败")