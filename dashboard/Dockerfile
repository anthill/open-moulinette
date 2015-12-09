FROM ubuntu:14.04


# install utilities 
RUN apt-get update && apt-get install -y \
    vim \
    git \
    wget \
    curl \
    screen \
    p7zip-full \
    unzip \
    fish \
    build-essential

# install nodejs 4.1
RUN curl --silent --location https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install -y nodejs

# install python with conda
RUN apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda-2.3.0-Linux-x86_64.sh && \
    /bin/bash /Anaconda-2.3.0-Linux-x86_64.sh -b -p /opt/conda && \
    rm /Anaconda-2.3.0-Linux-x86_64.sh && \
    /opt/conda/bin/conda install --yes conda==3.14.1
ENV PATH /opt/conda/bin:$PATH

# setup the shell
# RUN chsh -s `which fish`
# RUN mkdir -p ~/.config/fish/
# RUN touch ~/.config/fish/config.fish
# # RUN echo "set -gx PATH /opt/conda/bin $PATH" >  ~/.config/fish/config.fish
# CMD su root 



WORKDIR /open-moulinette/dashboard/src