# 298724892 folder
Files:
1) 00110001_Are_You_Afraid_of_the_Dark.png
1) 00110010_Phase_III.wav
1) 00110011_Arthur_Lang_Journal.pdf
1) Project_Eclipse.zip

Still not sure what's the binary numbers in filename. Could be:
- 49, 50 and 51 in decimal, maybe not
- '1', '2', '3' in ASCII, maybe more plausible, so just the file index?

## 00110001_Are_You_Afraid_of_the_Dark.png
Maximizing the exposure, a QR code could be found, that lead to a picture
https://loopgarden.io/Iris_Lang_515.jpg

## 00110010_Phase_III.wav
- Audio track say `Phase 2 was a success, phase 3 will begin shortly, all effort to secure - must be prioritized, she has become unpredictable, her proximity to - places her at risk at extended (maybe?)`
- Reversing the last seconds, the track say:
`Watch what you hear, see, don't listen`
- Looking at the song spectrogram, the initial noise write "24", still not sure what to do with that.
Also other songs' spectrogram has some embedded pictures

### 00110010_Phase_III spectogram 
![image](00110010_Phase_III_spectrum.png)

## 00110011_Arthur_Lang_Journal.pdf
```
Journal Entry – September 4th
The shadows grow heavier each day. I can feel their eyes even in the brightest rooms,
their whispers in the silence.
It wasn’t always like this. There was a time when Umbra’s goals felt noble, uniting
power to bring order. But order at what cost? Project Eclipse isn’t order, it’s
obliteration. Sirion will burn, and with it, the hope I once held.
I told Iris only fragments. She’s too bright, too full of life to be dragged into this
darkness. If they find out what I’ve done... if they uncover the letters... it won’t just be
me who pays the price.
They trust me, for now. But the crescent’s light is waning, and soon they’ll come. I
can’t stop it, not alone. Someone must, someone who’s not afraid of the dark.

Journal Entry – September 19th
Astraea was my greatest creation. A breakthrough in intelligence and insight. But in
the wrong hands, it could become a weapon. Umbra needs the keystone to complete
their plans. Without the keystone, Astraea is just lines of code. Brilliant, but lifeless.
It’s only a matter of time before they find it.
The truth lies where light and shadow meet. Those words hold the key. Time is
running out, but I can only hope this falls into the right hands.

Journal Entry – September 28th
Mlv otbcd wj mmtwqag. Bfzl wlexrcmg jhqvfpvnz, plm M tmv’g txzc aii, zwg yxh. Kai
kdcgh pcleh uqagrhm yxv re qg htg dx. Xyq abcbskr arfkuel smxvpfpvnz, plm imqv
ghxm uhr’k emr tas tketwa sokazgk.
Ktm qemstmmmq qf peopbrx fprik drkx nqty, thc nxpc. Pw ghxm bgsn ipnt mvvr’vv
opnsbbx? Hv rdm ghxm anwk mvbtasi ienz tvkx av?
Bj pac’ee ksrwmes buil, mfn’vv otbsx. Hyx eeeerr bge’m me ipnt rcl liv, ub’f ig kytx
pac qog’h. Ixqvyjrr: mvv vvvekrnm ocpepe xbighj mlv iil.

```

The last entry is a Vigenere code, the key is `TERMINATOR` 
(found use an [online decipher](https://www.dcode.fr/vigenere-cipher),
not sure how someone could guess that?).  
The deciphered text is:
```
The clock is ticking. Iris suspects something, but I can’t tell her, not yet. The
truth would destroy her as it has me. The society watches everything, but even
they don’t see the cracks forming.
The detective is playing their part well, too well. Do they know what they’re
chasing? Or are they just another pawn like me?
If you’re reading this, you’re close. The answer isn’t in what you see, it’s in what
you don’t. Remember: the crescent always points the way.
```

## Project_Eclipse.zip
The file is protected by password. I thought the lead was in some documents in the folder,
but I was stuck there.
With some help from
[John the Ripper](https://github.com/openwall/john)
```
$ zip2john Project_Eclipse.zip > Project_Eclipse_hash.txt
$ john --incremental Project_Eclipse_hash.txt
```
in just a few seconds the password was cracked, and it is `10241929`.
Still not a clue how someone could have found that, maybe the 24 is from the spectrogram of
00110010_Phase_III.wav  
By the way cracking this zip lead to 2 additional documents, check Project_Eclipse/README.md

