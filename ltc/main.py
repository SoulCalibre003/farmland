B
    I��\�$  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s�  d dl mZmZmZ d dlmZmZ d dlmZ d dlm	Z	 d dl
mZ d dlZd dlZd dlZd dlZyd dlZd dlmZ W n   ed� e��  Y nX d	Zej�d
�s�e�d
� ee� eej�dk r�ed� e�d� dd� Ze�� ZddiZdZdZ ejd Z!ede! ee �Z"e"�#�  e"�$� �svye"�%e!� e"�&e!e'd��Z(W n* ek
�rt   e'd�Z)e"�*e!e)�Z(Y nX e"�+� Z,e�-d� ee� ede,j.d� ed� �ze"�/d�Z0dZ1�x e2d�D �]�Z3ej4�5d� ej4�5d� ej4�5d� ej4�5d� ej4�6�  e"j7e0d d!� ed"� e"ee0ddd d d d d d#��Z8e8j9d  j:�;d$�d%k�rbed&� e��  �qĐyze8j9d  j<j=d  j>d  j?Z?ej4�5d� ej4�5d'e? � ej4�6�  e8j9d  j@Z@ejAe?ed(d)d*�ZBeeBjCd+�ZDeDj;d,d-d.�dk�r�eDj;d,d/d0�dk�r�ed� e"ee0ddd d d d d d#��Z8e8j9d  j:Z:e8j9d  j:�;d1�d%k�sXe8j9d  j:�;d2�d%k�r�e�Ed3e:�ZFeeGeFd  �� ed� e"ee0ddd d d d d d#��Z8e8j9d j:ZHed� ej4�5d4eH d5 � n �neDj;d,d/d0�dk	�r^x�eDjId,d6d.�D ]nZJeJ�Ad7�ZKeJ�Ad8�ZLeJ�Ad9�ZMeeGeL�� ejNd:eKeMd;�ed(d)d<�ZBe�OeBjP�ZQej4�5d=eQd>  d? � �q�W n~ej4�5d� ej4�5d@� ej4�5d� ej4�5dA� ej4�6�  ed� e"ee1e@e8j9d  j<j=d  j>d jRdB�� ej4�5dC� ed� W n�   ed"� e"ee0ddd d d d d d#��Z8e8j9d  j:Z:e8j9d  j:�;d1�d%k�sFe8j9d  j:�;d2�d%k�r�e�Ed3e:�ZFeeGeFd  �� ed� e"ee0ddd d d d d d#��Z8e8j9d j:ZHed� ej4�5d4eH d5 � n Y nX �q�W W de"�S�  X dS )D�    )�TelegramClient�sync�events)�GetHistoryRequest�GetBotCallbackAnswerRequest)�SessionPasswordNeededError)�FloodWaitError)�sleepN)�BeautifulSoupz�[1;30m# [1;31mHmmm Sepertinya Modul Requests Dan Bs4 Belum Terinstall
[1;30m# [1;31mTo install Please Type pip install requests and pip install bs4aT  [0;35m   ____               _                / ___|   ___ _    _| |               \___ \ / _  \| |  | | |                ___)  |  (_) |  |_| | |               |____/ \___/ \__,_|_|                      ____       _ _  _                    /  ___|__ _|  (_)  |__  _ __ ___      |  |   /  _`  |  |  | '_ \|  '__/ _ \     |  |__|  (_|  |  |  | |_)  |  | |   __/      \____\__,_ |_|_ |_.__/|_|  \___|                                    
[0;34m=========================================================
[1;32mAuthor By  [1;31m:[1;0m SoulCalibre
[1;32mFB Page Yt[1;31m : [1;0mSoulCalibre007session�   z$


[1;32mUsage : python main.py +62�   c             C   sb   t j�d� t j�d� xDt| dd�D ]4}t j�d� t j�d�|�� t j��  td� q&W d S )N�z?                                                               r   �����z,[1;30m#[1;0m{:2d} [1;32mseconds remainingr   )�sys�stdout�write�range�format�flushr	   )�xZ	remaining� r   � �tunggu!   s    
r   z
User-Agentz�Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36iq�
 Z 322526d2c3350b1d3530de327cf08c07zsession/z 


[1;0mEnter Your Code Code : z[1;0mYour 2fa Password : �clearz[1;32mWelcome To Autobot8
[1;32mAutobot For LTC Click Bot

z[1;37mPlease wait......!z@Litecoin_click_boti@KL r   z>                                                              z%[1;30m# [1;33mConnecting to:u   🖥 Visit sites)Zentity�message�   )ZpeerZlimitZoffset_dateZ	offset_idZmax_idZmin_idZ
add_offset�hashz%Sorry, there are no new ads availabler   z3
[1;30m# [1;31mIklan Sudah Habis Coba Lagi Besok
z[1;30m# [1;33mVisit �   T)�headers�timeout�allow_redirectszhtml.parserZdivzg-recaptcha)Zclass_Zheadbar)�idzYou must stayzPlease stay onz([\d.]*\d+)z[1;30m# [1;32m�
zcontainer-fluidz	data-codez
data-timerz
data-tokenzhttps://dogeclick.com/reward)�codeZtoken)�datar   r   r    z[1;30m# [1;32mYou earned Zrewardz LTC for visiting a site!
z@                                                                z [1;30m# [1;31mError! Click SKIP)r$   z)[1;30m# [1;31mSkip Captcha...!       
)TZtelethonr   r   r   Ztelethon.tl.functions.messagesr   r   Ztelethon.errorsr   r   Ztimer	   Zjson�rer   �osZrequestsZbs4r
   �print�exitZbanner�path�exists�makedirs�len�argvr   ZSession�cZuaZapi_idZapi_hashZphone_numberZclientZconnectZis_user_authorizedZsend_code_requestZsign_in�input�meZpassw�startZget_meZmyself�systemZ
first_nameZ
get_entityZchannel_entityZchannel_usernamer   �ir   r   r   Zsend_messageZpostsZmessagesr   �findZreply_markupZrowsZbuttonsZurlr!   �get�rZcontentZsoupZfindallZsec�intZ
messageresZfind_allZdatr#   ZtimerZtokenaZpost�loads�textZjsr$   Z
disconnectr   r   r   r   �<module>   s�    









(0


 
 0)�marshal�exec�loads� r   r   �out.py�<module>   s   