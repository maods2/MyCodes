

[wav_1, fs] = audioread('Skrilex.wav');

audio = wav_1(:, 1).';

fc = 4000;                                      % Frequência de Corte
    
M = 20;                                        % Ordem do Filtro
    
n=[0:M-1];

wc = 2 * pi * fc * (1/fs) ;                     % Frequência de Corte Normalizada

w_bart = (1 - ((2*abs(n - (M-1)/2))/(M-1)))';   % Janela de Bartlett

%w_bart = bartlett(M); 
%w_bart = hanning(M);

hd = (wc/pi)*sinc((wc/pi)*(n - M/2));           % Filtro Low Pass
   
h=hd'.*w_bart;                                  % Resposta ao Impulso Unitário

filtrado = conv(audio,h);                       % Convolução h[n]*x[n]

fftf(audio,fs);                                 % FFT Sinal original

fftf(filtrado,fs);                              % FFT Sinal Filtrado

audiowrite('Audio_Filtrado_Matlab.wav',filtrado,fs)   % Salvando audio Filtrado


function [X, freq] = fftf(x, Fs)                % Função para FFT


N=length(x);
K=0:N-1;
T=N/Fs;
freq=K/T;
X=fftn(x)/N;
cutOff=ceil(N/2);
X=X(1:cutOff);

figure();
plot(freq(1:cutOff), abs(X));
title('Sinal Original');
xlabel('Frequência (HZ)');
ylabel('Amplitude');
end