# DP_scratch
밑바닥부터 시작하는 딥러닝 실습하기

## 개발 환경 만들기
> vscode에서 가상환경을 만들어 봅시다.
> 가상환경은 독립된 공간을 만들어 프로젝트에 사용되는 패키지들이 구분될 수 있도록 해줍니다.
> 
> 1. 가상환경을 구축할 폴더를 만들어 줍니다.
> ```
> ~> python -m venv [가상환경 이름]
> ~> python -m venv scratch
> ```
> 위 명령어를 실행하면 scratch 라는 이름의 공간이 만들어지고 그 공간은 상위 폴더의 코딩 환경을 그대로 이어받게 됩니다.
> 
> 2. 가상환경 파일로 들어갑니다.
> ```
> ~> cd [가상환경 이름]
> ~> cd scratch
> ```
> 
> 3. 가상환경을 활성화 합니다.
> ```
> ~\[가상환경 이름]> .\Scripts\Activate.ps1
> ~\scratch> .\Scripts\Activate.ps1
> ```
> 활성화 하게 되면 앞에 (scratch) 가 붙게 됩니다.
> ```
> (scratch) ~\scratch>
> ```
> 
> 4. 가상환경 비활성화
> ```
> (scratch) ~\scratch> deactivate
> ```
> 
> 5. 가상환경을 기본 인터프리터로 설정하기
> f1키를 누르고 Pythone: Select Interpreter 항목을 찾습니다.
> 뒤에 (scratch) 라고 적혀있는 항목을 선택합니다.
