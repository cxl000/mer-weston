%define with-cairo no
%define with-xwayland no
Name:           weston
Version:        6.0.1
Release:        1
Summary:        Wayland Compositor Infrastructure
License:        MIT
Group:          System/GUI/Other
Url:            https://github.com/wayland-project/weston
Source:         %name-%version.tar.xz
#Patch1:         000_simple_clients_programs_LDADD.patch
# libvpx-dev libva-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev freerdp2-dev curl python3-pip python3-setuptools
BuildRequires:  pkgconfig(expat)
BuildRequires:  libffi-devel
BuildRequires:  pkgconfig(mtdev) >= 1.1.0
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
#BuildRequires:  xmlto				# package home:plfiorini:maui:devel / xmlto
BuildRequires:  doxygen
#BuildRequires:  graphviz		   # package mint / graphviz
#BuildRequires:  linux-libc-dev
BuildRequires:  pkgconfig(xkbcommon) >= 0.0.578
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client) >= 1.0.0
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:	pkgconfig(libinput)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libdrm) >= 2.4.30
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libpng)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libudev) >= 136
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(egl) >= 7.10
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  libxml2-devel

BuildRequires:  llvm-devel
BuildRequires:	pkgconfig(libunwind)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:  pkgconfig(libgcrypt)
#BuildRequires:  pkgconfig(xorg-x11-proto-scrnsaver)
BuildRequires:  pkgconfig(libedit)
#BuildRequires:  libpciaccess-dev
#BuildRequires:  libgudev-1.0-dev
#BuildRequires:  python3-mako                
#BuildRequires:  libxfont-dev

%if "%{with-xwayland}" == "yes"
#libxcb-xkb-dev
#libgdk-pixbuf2.0-dev libxcursor-dev
#CXL#BuildRequires:	pkgconfig(xcursor)
BuildRequires: libxcb-composite0-dev
BuildRequires: pkgconfig(xorg-x11-proto-randr)
BuildRequires: pkgconfig(xorg-x11-proto-composite)
BuildRequires: pkgconfig(xorg-x11-proto-xinerama)
BuildRequires: pkgconfig(xorg-x11-proto-dri2)
BuildRequires: pkgconfig(xorg-x11-proto-gl)
BuildRequires: xutils-dev
BuildRequires: libxcursor-dev
BuildRequires: libx11-dev
BuildRequires:	pkgconfig(xcb)
#BuildRequires: x11proto-dri3-dev
BuildRequires: libxdamage-dev
BuildRequires: libxext-dev
BuildRequires: libxfixes-dev
#CXL#BuildRequires:	pkgconfig(xcb-xfixes)
BuildRequires: libxxf86vm-dev
%endif
#CXL##BuildRequires:  libvpx-devel
#CXL##BuildRequires:  rsvg-view
#CXL#BuildRequires:	xkeyboard-config
#CXL#%if "%{with-cairo}" == "yes"
#CXL#BuildRequires:  pkgconfig(cairo-egl) >= 1.11.3
#CXL#BuildRequires:	pkgconfig(cairo-xcb)
#CXL#%endif
#CXL#BuildRequires:  pkgconfig(gio-2.0)
#CXL##BuildRequires:  gfx-rpi-libGLESv2-devel
#CXL#BuildRequires:  pkgconfig(libsystemd-login)
#CXL#BuildRequires:  pkgconfig(poppler-glib)
Requires:	xkeyboard-config

%description
Weston is the reference implementation of a Wayland compositor, and a
useful compositor in its own right. Weston has various backends that
lets it run on Linux kernel modesetting and evdev input as well as
under X11. Weston ships with a few example clients, from simple
clients that demonstrate certain aspects of the protocol to more
complete clients and a simplistic toolkit. There is also a quite
capable terminal emulator (weston-terminal) and an toy/example
desktop shell. Finally, weston also provides integration with the
Xorg server and can pull X clients into the Wayland desktop and act
as a X window manager.

%package devel
Summary:    Weston SDK
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Weston SDK files

%prep
%setup -q -n %{name}-%{version}
#%patch1 -p1

%build
cd upstream
%meson \
	-Dbackend-drm=true \
	-Dbackend-drm-screencast-vaapi=false \
	-Dbackend-headless=true \
	-Dbackend-rdp=false \
	-Dbackend-wayland=true \
	-Dbackend-x11=false \
	-Dbackend-fbdev=true \
	-Dbackend-default=drm \
	-Drenderer-gl=false \
	-Dweston-launch=true \
	-Dxwayland=false \
	-Dsystemd=true \
	-Dremoting=false \
	-Dshell-desktop=true \
	-Dshell-fullscreen=true \
	-Dshell-ivi=true \
	-Ddesktop-shell-client-default=weston-desktop-shell \
	-Dcolor-management-lcms=true \
	-Dcolor-management-colord=false \
	-Dlauncher-logind=true \
	-Dimage-jpeg=true \
	-Dimage-webp=true \
	-Dtools=calibrator,debug,info,terminal,touch-calibrator \
	-Dsimple-dmabuf-drm=freedreno \
	-Ddemo-clients=true \
	-Dsimple-clients=damage,im,shm,touch,dmabuf-v4l \
	-Dresize-pool=true \
	-Dwcap-decode=true \
	-Dtest-junit-xml=true
#	-Dpipewire=false
#	-Ddoc=false
#	simple-dmabuf-drm=freedreno #, choices: [ auto, intel, freedreno, etnaviv ],
#	xwayland-path=/usr/bin/Xwayland,
%meson_build
cd ..

%install
cd upstream
%meson_install
rm -f "%buildroot/%_libdir"/*.la "%buildroot/%_libdir/weston"/*.la;
cd ..

%check
mkdir -pm go-rwx xdg;
# Ignore exit code, because """the headless backend is not even in the 1.0
# stable series. It means it will be an option starting from 1.2 of stable
# series."""
XDG_RUNTIME_DIR="$PWD/xdg" make check || :;

%files
%defattr(-,root,root)
%{_bindir}/wcap-*
%{_bindir}/weston*
%{_libexecdir}/weston-*
%{_libdir}/weston
%{_libdir}/libweston-6.so*
%{_libdir}/libweston-desktop-6.so*
%{_libdir}/libweston-6/*-backend.so
%{_datadir}/libweston
%{_datadir}/wayland-sessions/weston.desktop
%{_mandir}/man1/weston*.1*
%{_mandir}/man7/weston*7*


%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/weston-6.pc
%{_libdir}/pkgconfig/weston-desktop-6.pc
%{_datadir}/pkgconfig/libweston-6-protocols.pc
%{_datadir}/libweston/protocols/weston-debug.xml
%doc %{_mandir}/man5/weston.ini.5.gz
# >> files devel
# << files devel


