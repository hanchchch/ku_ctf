from base64 import urlsafe_b64encode
from passlib.hash import bcrypt_sha256
import os

admin_id = 'admin'
admin_email = 'cndghks15@gmail.com'
admin_pw = urlsafe_b64encode((os.urandom(33)))
admin_pw = b'qcp7iXp25vCiCg6UjY1Okc-87bhyQee4V6LaxfKXOGAB'
admin_pw_hash = bcrypt_sha256.hash(admin_pw)

config = {
    'ctf_version': '3.1.1',
    'ctf_theme': 'core',
    'ctf_name': 'KU CTF',
    'ctf_description': '',
    'user_mode': 'teams',
    'start': '1604653200',
    'end': '1604696400',
    'freeze': None,
    'challenge_visibility': 'private',
    'registration_visibility': 'public',
    'score_visibility': 'public',
    'account_visibility': 'public',
    'verify_emails': None,
    'mail_server': None,
    'mail_port': None,
    'mail_tls': None,
    'mail_ssl': None,
    'mail_username': None,
    'mail_password': None,
    'mail_useauth': None,
    'verification_email_subject': 'Confirm your account for {ctf_name}',
    'verification_email_body': 'Please click the following link to confirm your email address for {ctf_name}: {url}',
    'successful_registration_email_subject': 'Successfully registered for {ctf_name}',
    'successful_registration_email_body': "You've successfully registered for {ctf_name}!",
    'user_creation_email_subject': 'Message from {ctf_name}',
    'user_creation_email_body': 'An account has been created for you for {ctf_name} at {url}. \n\nUsername: {name}\nPassword: {password}',
    'password_reset_subject': 'Password Reset Request from {ctf_name}',
    'password_reset_body': "Did you initiate a password reset? If you didn't initiate this request you can ignore this email. \n\nClick the following link to reset your password:\n{url}",
    'password_change_alert_subject': 'Password Change Confirmation for {ctf_name}',
    'password_change_alert_body': "Your password for {ctf_name} has been changed.\n\nIf you didn't request a password change you can reset your password here: {url}",
    'setup': '1',
    'theme_header': '<style id="theme-color">\r\n:root {--theme-color: #000000;}\r\n.navbar{background-color: var(--theme-color) !important;}\r\n.jumbotron{background-color: var(--theme-color) !important;}\r\n</style>\r\n',
    'theme_footer': '',
    'theme_settings': ''
}

pages = (1, None, 'index', """<div class="row">
	<div class="col-md-8 offset-md-2">
		<img class="w-100 mx-auto d-block" style="max-width: 700px;padding-bottom: 50px;padding-top: 14vh;" src="themes/core/static/img/ctf_logo.png" />
		<br>
		<div style="display: flex; flex-direction: row; align-items: center; justify-content: space-around; margin-top: 5vh;">
			<span><img style="max-width: 30px; max-height: 30px; padding: 2px;" src="themes/core/static/img/ku_logo.png" /> Korea University</span>
			<span><img style="max-width: 30px; max-height: 30px;" src="themes/core/static/img/cs_logo.png" /> College of Informatics</span>
			<span><img style="max-width: 30px; max-height: 30px; padding: 2px;" src="themes/core/static/img/cydf_logo.png" /> Division of Information Security</span>
			<span><img style="max-width: 30px; max-height: 30px;" src="themes/core/static/img/cykor_logo.png" /> CyKor</span>
		</div>
	</div>
</div>""", 0, None, None)

teams = [
    (1, None, "College of Informatics", None, 
    "$bcrypt-sha256$2b,12$PTE1mHfqzup5CT6Um6sG2e$guR3whXZawBG6FjvtnVLSyB7.visxNy",
    None, None, None, None, None,
    0, 0, 0,
    "2020-10-24 08:26:05.036659"),
    (2, None, "Division of Information Security", None, 
    "$bcrypt-sha256$2b,12$PTE1mHfqzup5CT6Um6sG2e$guR3whXZawBG6FjvtnVLSyB7.visxNy",
    None, None, None, None, None,
    0, 0, 0,
    "2020-10-24 08:26:05.036659"),
]

users = [(1, None, admin_id, 
    admin_pw_hash, 
    admin_email,
    "admin",
    None, None, None, None, None, 
    1, 0, 0, 2,
    "2020-10-24 08:15:36.814443")]

notifications = [
    (4, 'Rules', '''
1. 진행 시간: 11/6 18:00 ~ 11/7 06:00<br>
2. flag format: KOREA{zzz}<br>
3. 참가자는 문제에서 주어진 서버만을 대상으로 공격을 시도해야 합니다.<br>
4. 문제에 대한 질문이 있을 시 해당되는 help 채널에 admin을 멘션하고 문제 이름을 명시해주시기 바랍니다(ex. @admin koreaspa-pwn 질문 있습니다). 문제에 대한 질문 이외의 문의사항이 있을 시 etc 채널을 이용해주시기 바랍니다.<br>
5. 디스코드 채널에서 문제 풀이에 직접적인 힌트가 될 수 있는 내용을 공유하거나, 대회와 관련 없는 사담을 나누는 참가자는 운영진이 임의로 제재할 수 있습니다.''', '2020-11-06 00:00:00.0000000', None, None),
    (3, '!Caution!', '''
- 학번은 대회 종료 이후 상품 지급을 위한 본인 확인에 사용됩니다. 한 번 등록한 학번은 수정할 수 없습니다.<br>
- 참가자는 본인이 재학 중인 학부에 해당하는 팀을 선택해야 합니다. 한 번 선택한 팀은 수정할 수 없습니다.<br>''', '2020-11-06 00:00:00.0000000', None, None),
    (2, 'Contact', '''디스코드 채널<br>
- https://discord.gg/Vh9zvSspkQ<br>
- 디스코드 채널에서는 대회가 진행되는 동안 문제에 대한 질문 등을 포함하여 참가자와 운영진 간의 질의응답과 공지사항 전달이 이루어집니다.''', '2020-11-06 00:00:00.0000000', None, None),
    (1, 'Challenge Colors', '''
- 팀에서 아무도 풀지 않은 문제는 회색으로 표시 됩니다. 솔브 가능한 상태입니다.<br><img src="/themes/core/static/img/no_solve.png"><br>
- 팀에서 누군가 풀은 문제는 어두운 초록색으로 표시 됩니다. 솔브 가능한 상태입니다.<br><img src="/themes/core/static/img/team_solve.png"><br>
- 자신이 풀은 문제는 밝은 초록색으로 표시 됩니다. 솔브 불가능한 상태입니다.<br><img src="/themes/core/static/img/me_solve.png"><br>''', '2020-11-06 00:00:00.0000000', None, None)
]