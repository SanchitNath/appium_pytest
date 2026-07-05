# Appium Pytest framework to launch an application on an emulator

-----------------------------------

### Installation Steps
1. Configure and install JDK
```bash
  brew install openjdk@17
  sudo ln -sfn /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk
  Open terminal
  nano ~/.zshrc
  export JAVA_HOME=/opt/homebrew/opt/openjdk@17
  Press Ctrl + O, then hit Enter, then press Ctrl + X
  source ~/.zshrc
  java --version
```
2. Install Node.js, adb via brew
```bash
  brew --verion
  brew install node
  node --version
  brew install android-platform-tools
```
3.Download apk under apps (Not needed if you are using emulator with playstore)
```bash
  curl -L -k -o flipkart.apk "https://github.com"
```
4. Install android studio and configure the ANDROID_HOME path
```bash
  brew install --cask android-studio 
  or download the latest one from https://developer.android.com/studio
  nano ~/.zshrc
  export ANDROID_HOME=/Users/<username>/Library/Android/sdk
  export PATH=$PATH:$ANDROID_HOME/emulator
  export PATH=$PATH:$ANDROID_HOME/tools
  export PATH=$PATH:$ANDROID_HOME/tools/bin
  export PATH=$PATH:$ANDROID_HOME/platform-tools
  Press Ctrl + O, then hit Enter, then press Ctrl + X
  source ~/.zshrc
  Open the android studio
  Open virtual device manager to create a new emulator with the required configuration
  Press play button
  Open playstore and download the app
```
5. Run the appium server command
```bash
  npm install -g appium
  appium --version
  appium driver install uiautomator2
  appium
```
6. Run adb command to view the connected devices if android studio emulator is running
```bash
  adb devices
    * daemon not running; starting now at tcp:5037
    * daemon started successfully
    List of devices attached
    emulator-****   device
```
7. Install appium client libraries for Python
```bash
  cd main
  python3 -m venv venv_test
  source venv_test/bin/activate
  pip install Appium-Python-Client
```
8. To install requirement from pyproject.toml file & run the test cases
```bash
    python3 -m pip install -e .
    It creates 'playwright_pytest_framework.egg-info' folder
```
9. To run the test cases, use the following command:
```bash
  cd main
  python3 -m pytest -s tests/test.py
```