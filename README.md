# 책영감
## Brief overview

Interactive Reading에 도움을 주는 서비스, 책영감.   
<br/>
<책영감>은 책 읽을 때 오래 기억하고 싶은 부분을 남기기 위해 책 속 구절 사진을 찍으면 메모처럼 저장되는 앱입니다.    
업로드 된 책 이미지 속의 텍스트를 인식한 후 사용자가 입력한 간단한 메모, 감상, 날짜 등과 함께 독서노트에 기록됩니다.   

![18](https://user-images.githubusercontent.com/50884017/159531151-9bdf093c-6b4a-47e3-ab54-f352c67574f2.png)

책영감은 왜 필요할까요?    
적극적인 독서 활동은 독서 능률을 증진시킵니다.   
또한 많은 사용자들이 다양한 독서 서비스 어플들을 사용하고 있는데요, 이는 interactive reading에 대한 수요층이 굉장히 많다는 것을 의미하기도 합니다.    
하지만, 관련 앱의 리뷰를 보면 사진 '업로드에 시간이 너무 많이 걸린다.', '데이터 사용량이 너무 많다.', '로그인 기능이 없다.' 라는 피드백이 많았습니다.   

그래서 책영감은 기존 서비스와 차별성을 두기위해 OCR기능을 추가했습니다.    
이미지가 아닌 텍스트로 저장함으로써 데이터 소모를 줄일 뿐 아니라, 사용자가 원하는 부분만 편집하여 저장할 수 있게 하였습니다.     
로그인 기능도 제공하여 사용자 개개인의 데이터를 로그인만 하면 어디서든 확인할 수 있게 하였습니다.     


<br/><br/>

## How to run project
### Install
```
$ git clone https://github.com/di-uni/bookinspire.git
$ minikube start
$ docker build -f Dokerfile -t bookgam .
$ kubectl create -f k8s/
$ ngrok http 30001
```  
Open ngrok link in browser to access this program.

<br/><br/>

## Detailed description

### 1) Home / Login / Register
- **Home**
	- 홈 페이지에서는 로그인(또는 회원가입 후 로그인)을 하면 그동안 작성한 책 감상문을 보거나 새로운 감상문을 작성할 수 있습니다. 
	- There is a path where you can log in, register, read data, and write data.
- **Login**
	- 아이디와 비밀번호를 통해 로그인을 할 수 있습니다. 
	- Users can login with ID and password.
- **Register**
 	- 회원가입을 위해서는 닉네임, ID, 그리고 비밀번호와 같은 정보가 필요합니다.
	- To register, nickname, ID, and password are required.   

<img height="300" alt="image" src="https://user-images.githubusercontent.com/50884017/159525424-6fca04fc-7d3c-489d-b776-97f36c4a1f1d.png">
<img height="350" alt="image" src="https://user-images.githubusercontent.com/50884017/159531997-3b554aba-98a5-42b9-a8c4-02e5d1eb48ba.png">

<br/>

### 2) Write the book report      
- **Image upload**
	- 책 이미지를 업로드하면, ocr 과정을 거쳐 이미지 속 텍스트를 추출할 수 있습니다.
	- To get the paragraphs of the book, upload the image of the book and wait for ocr.   
- **Write**
	- 독서 감상문을 완성하기 위해 책 제목, 작가, 읽은 날짜, 페이지, 그리고 자신의 생각을 입력합니다.
	- 등록하기를 누르면, 홈으로 돌아가고, 홈에서는 추가된 독서 감상문을 확인할 수 있습니다.
	- Write book title, author, read date, page and your own thought to complete the book report.
	- After register the book report, you can view the saved data by clicking the saved data list in Home.
<img height="400" alt="image" src="https://user-images.githubusercontent.com/50884017/159528575-fada737b-b047-42b7-b825-e92474ee3039.png">

<br/><br/>

## Technology stack
![10](https://user-images.githubusercontent.com/50884017/159532279-94997e51-ad7e-4c24-97c2-8c8827cbb899.png)

flask-based backend and an html + css frontend.

- **flask** : main_server.py(main program), parser.py(ocr data parse program)
   - Implementation of pagination
   - Image source storage
   - User data storage through sessions

- **html, css**: home.html, login.html etc (using with flask)
   - responsive UI (with flex)
   - able to use in web and mobile
   - customize various components

- **http, grpc**: Protocol used for communication between programs

- **ngrok** : program that allows external access to a specific port on the server.

- **redis** : user database

- **Naver OCR** : Process the image source saved by the user to extract text

- **Docker + k8s** : To provide containers and its orchestration for microarchitecture services  
  
![13](https://user-images.githubusercontent.com/50884017/159532400-e299eac1-d38d-4bbd-8fcd-c3b395b34ba6.png)

<br/><br/>

## Structures

- main_server.py: Main server that communicate other servers and client
- ocr_request.py: Receive data by communicating with Naver API
- parser.py: Parses the data received from Naver API and sends the desired text
  
<br/><br/>

## Responsive web
Demo in mobile

<img width="200" alt="회원가입" src="https://user-images.githubusercontent.com/50884017/159539010-b40aac15-d6f8-4e53-a6d3-d15bf4fd69bb.gif"> <img width="200" alt="로그인" src="https://user-images.githubusercontent.com/50884017/159539297-2406c6cd-2055-4c33-8f15-10c019db9eab.gif"> <img width="200" alt="작성" src="https://user-images.githubusercontent.com/50884017/159539582-b97ac125-aeb6-4b04-81ce-d3249540b4f8.gif">


<br/><br/>

## Detailed description of the main server

1. How to connect flask and html
```
@app.route('/', methods=['GET', 'POST'])
def home():
~~
	return render_template('home.html',currentUser=currentUser,users=pagination_data,page=page,per_page=per_page,pagination=pagination,total = total)

```

2. Pagination implementation
```
def get_page_data(offset=0, per_page=5, data = []):
    return data[offset: offset + per_page
pagination_data = get_page_data(offset = offset, per_page = per_page, data = data)
pagination = Pagination(page=page, per_page=per_page, total=total)
```

3. User data storage method
```
bookTitle = request.form.get("bookTitle")
redis.set(currentUser+"_bookTitle"+str(book_num),bookTitle)
```

4. image storage knowledge
```
image = request.files["image"]
image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
send_from_directory(app.config["IMAGE_UPLOADS"], filename)
```

5. move data between html
```
<h3><a onclick="location.href='/upload-image'">작성하기</a></h3>
or
<td><a href="{{ url_for('read', my_var=loop.index + (page - 1) * per_page) }}"> {{ user[0] }} Title </a></td>

```


<br/><br/>

## 역할 분담
- 박지윤: 주제에 대한 아이디어, UI, 시스템 구상, main server, 작성하기 페이지의 html, 반응형 웹을 고려한 모든 css
- 김태균: 시스템 구상, 전반적인 백엔드, 홈/로그인/회원가입 페이지의 html

<br/><br/>


## Credits
- grpc guide: https://developers.google.com/protocol-buffers/docs/pythontutorial
- 네이버 ocr api: https://guide.ncloud-docs.com/docs/ocr-ocr-1-4

<br/><br/>

## License

 MIT License   

Copyright (c) 2021 Jiyun Park
     
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
     
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
     
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

