FROM debian:stable-slim

ENV USER_NAME_1K=demo

RUN useradd -rm -d /home/${USER_NAME_1K} -s /bin/bash -g root -G sudo -u 1000 ${USER_NAME_1K}

RUN apt-get update \
    && apt-get install -y --no-install-recommends openssh-server sudo net-tools iproute2 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

RUN echo -n "${USER_NAME_1K}:${USER_NAME_1K}" | chpasswd

CMD [ "/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config" ]
