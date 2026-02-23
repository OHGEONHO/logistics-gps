[app]

# (str) 앱 이름 (기사님들 휴대폰에 표시될 이름)
title = LogisticsGPS

# (str) 패키지 명 (소문자 영문)
package.name = logistics_gps

# (str) 패키지 도메인
package.domain = com.yourcompany

# (str) 소스코드 위치
source.dir = .

# (list) 포함할 파일 확장자
source.include_exts = py,png,jpg,kv,atlas

# (str) 버전
version = 0.1

# (list) 필수 라이브러리 (requests와 GPS 제어용 plyer 포함)
# 핵심: requests 작동을 위해 certifi, idna 등 의존성 라이브러리를 명시함
requirements = python3,kivy==2.2.1,requests,plyer,urllib3,certifi,idna,charset-normalizer

# (list) 화면 방향 (세로 모드 고정)
orientation = portrait

#
# Android specific
#

# (bool) 전체화면 여부
fullscreen = 0

# (list) 안드로이드 권한 (GPS 및 인터넷 필수)
# 핵심: 기사님 폰의 정밀 위치와 백그라운드 서비스를 위한 권한 추가
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, FOREGROUND_SERVICE

# (int) 타겟 API 레벨 (최신 안드로이드 대응)
android.api = 33

# (int) 최소 지원 API 레벨 (안드로이드 5.0 이상)
android.minapi = 21

# (bool) 화면 꺼짐 방지 (위치 추적 중 중단 방지)
android.wakelock = True

# (list) 지원 아키텍처 (최신 폰 대응을 위해 arm64-v8a 포함)
android.archs = arm64-v8a

# (bool) 백업 허용
android.allow_backup = True

# (str) 앱 테마
android.apptheme = "@android:style/Theme.NoTitleBar"

[buildozer]

# (int) 로그 레벨 (2로 설정하면 빌드 에러 확인이 쉬움)
log_level = 2

# (int) 루트 실행 경고 표시
warn_on_root = 1

# (str) 빌드 결과물 저장 경로
# bin_dir = ./bin
