#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Thunar
Version  : 1.8.12
Release  : 41
URL      : http://archive.xfce.org/src/xfce/thunar/1.8/thunar-1.8.12.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/thunar/1.8/thunar-1.8.12.tar.bz2
Summary  : Modern file manager for Xfce
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: Thunar-bin = %{version}-%{release}
Requires: Thunar-data = %{version}-%{release}
Requires: Thunar-lib = %{version}-%{release}
Requires: Thunar-license = %{version}-%{release}
Requires: Thunar-locales = %{version}-%{release}
Requires: Thunar-man = %{version}-%{release}
Requires: Thunar-services = %{version}-%{release}
Requires: gvfs
BuildRequires : docbook-xml
BuildRequires : exiv2-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gvfs
BuildRequires : intltool
BuildRequires : libexif-dev
BuildRequires : libnotify-dev
BuildRequires : libxfce4util-lib
BuildRequires : libxslt-bin
BuildRequires : pcre-dev
BuildRequires : perl
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(exo-1)
BuildRequires : pkgconfig(exo-2)
BuildRequires : pkgconfig(garcon-1)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libwnck-1.0)
BuildRequires : pkgconfig(libxfce4kbd-private-3)
BuildRequires : pkgconfig(libxfce4panel-1.0)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(pango)
BuildRequires : sed

%description
Thunar GTK Style Properties
===========================
Several user interface elements in Thunar are customizable via the standard
GTK style mechanism. Besides the customization provided by the GTK widgets,
that are used in Thunar, there are a bunch of additional settings that can
be customized via the GTK theme or the ~/.gtkrc-2.0 file in the users home
directory.

%package bin
Summary: bin components for the Thunar package.
Group: Binaries
Requires: Thunar-data = %{version}-%{release}
Requires: Thunar-license = %{version}-%{release}
Requires: Thunar-services = %{version}-%{release}

%description bin
bin components for the Thunar package.


%package data
Summary: data components for the Thunar package.
Group: Data

%description data
data components for the Thunar package.


%package dev
Summary: dev components for the Thunar package.
Group: Development
Requires: Thunar-lib = %{version}-%{release}
Requires: Thunar-bin = %{version}-%{release}
Requires: Thunar-data = %{version}-%{release}
Provides: Thunar-devel = %{version}-%{release}
Requires: Thunar = %{version}-%{release}
Requires: Thunar = %{version}-%{release}

%description dev
dev components for the Thunar package.


%package doc
Summary: doc components for the Thunar package.
Group: Documentation
Requires: Thunar-man = %{version}-%{release}

%description doc
doc components for the Thunar package.


%package lib
Summary: lib components for the Thunar package.
Group: Libraries
Requires: Thunar-data = %{version}-%{release}
Requires: Thunar-license = %{version}-%{release}

%description lib
lib components for the Thunar package.


%package license
Summary: license components for the Thunar package.
Group: Default

%description license
license components for the Thunar package.


%package locales
Summary: locales components for the Thunar package.
Group: Default

%description locales
locales components for the Thunar package.


%package man
Summary: man components for the Thunar package.
Group: Default

%description man
man components for the Thunar package.


%package services
Summary: services components for the Thunar package.
Group: Systemd services

%description services
services components for the Thunar package.


%prep
%setup -q -n thunar-1.8.12
cd %{_builddir}/thunar-1.8.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580495900
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --disable-introspection
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1580495900
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Thunar
cp %{_builddir}/thunar-1.8.12/COPYING %{buildroot}/usr/share/package-licenses/Thunar/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/thunar-1.8.12/COPYING.LIB %{buildroot}/usr/share/package-licenses/Thunar/86207ea3fdd7e8ef5ea34ca9d12a511dc7272d31
%make_install
%find_lang thunar
## Remove excluded files
rm -f %{buildroot}/usr/share/dbus-1/services/org.freedesktop.FileManager1.service
## install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/. && rmdir %{buildroot}%{_sysconfdir}

## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/Thunar/ThunarBulkRename
/usr/lib64/Thunar/thunar-sendto-email

%files bin
%defattr(-,root,root,-)
/usr/bin/Thunar
/usr/bin/thunar
/usr/bin/thunar-settings

%files data
%defattr(-,root,root,-)
/usr/share/Thunar/sendto/thunar-sendto-email.desktop
/usr/share/applications/thunar-bulk-rename.desktop
/usr/share/applications/thunar-settings.desktop
/usr/share/applications/thunar.desktop
/usr/share/dbus-1/services/org.xfce.FileManager.service
/usr/share/dbus-1/services/org.xfce.Thunar.FileManager1.service
/usr/share/dbus-1/services/org.xfce.Thunar.service
/usr/share/icons/hicolor/128x128/apps/Thunar.png
/usr/share/icons/hicolor/16x16/apps/Thunar.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_folder-copy.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_folder-move.png
/usr/share/icons/hicolor/24x24/apps/Thunar.png
/usr/share/icons/hicolor/24x24/stock/navigation/stock_folder-copy.png
/usr/share/icons/hicolor/24x24/stock/navigation/stock_folder-move.png
/usr/share/icons/hicolor/48x48/apps/Thunar.png
/usr/share/icons/hicolor/64x64/apps/Thunar.png
/usr/share/icons/hicolor/scalable/apps/Thunar.svg
/usr/share/metainfo/org.xfce.thunar.appdata.xml
/usr/share/pixmaps/Thunar/Thunar-about-logo.png
/usr/share/polkit-1/actions/org.xfce.thunar.policy
/usr/share/xdg/Thunar/uca.xml
/usr/share/xfce4/panel/plugins/thunar-tpa.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/thunarx-3/thunarx/thunarx-config.h
/usr/include/thunarx-3/thunarx/thunarx-file-info.h
/usr/include/thunarx-3/thunarx/thunarx-menu-item.h
/usr/include/thunarx-3/thunarx/thunarx-menu-provider.h
/usr/include/thunarx-3/thunarx/thunarx-menu.h
/usr/include/thunarx-3/thunarx/thunarx-preferences-provider.h
/usr/include/thunarx-3/thunarx/thunarx-property-page-provider.h
/usr/include/thunarx-3/thunarx/thunarx-property-page.h
/usr/include/thunarx-3/thunarx/thunarx-provider-factory.h
/usr/include/thunarx-3/thunarx/thunarx-provider-module.h
/usr/include/thunarx-3/thunarx/thunarx-provider-plugin.h
/usr/include/thunarx-3/thunarx/thunarx-renamer-provider.h
/usr/include/thunarx-3/thunarx/thunarx-renamer.h
/usr/include/thunarx-3/thunarx/thunarx.h
/usr/lib64/libthunarx-3.so
/usr/lib64/pkgconfig/thunarx-3.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/thunar/README.gtkrc
/usr/share/gtk-doc/html/thunarx/ThunarxFileInfo.html
/usr/share/gtk-doc/html/thunarx/ThunarxMenu.html
/usr/share/gtk-doc/html/thunarx/ThunarxMenuItem.html
/usr/share/gtk-doc/html/thunarx/ThunarxMenuProvider.html
/usr/share/gtk-doc/html/thunarx/ThunarxPreferencesProvider.html
/usr/share/gtk-doc/html/thunarx/ThunarxPropertyPage.html
/usr/share/gtk-doc/html/thunarx/ThunarxPropertyPageProvider.html
/usr/share/gtk-doc/html/thunarx/ThunarxProviderFactory.html
/usr/share/gtk-doc/html/thunarx/ThunarxProviderPlugin.html
/usr/share/gtk-doc/html/thunarx/ThunarxRenamer.html
/usr/share/gtk-doc/html/thunarx/ThunarxRenamerProvider.html
/usr/share/gtk-doc/html/thunarx/abstraction.png
/usr/share/gtk-doc/html/thunarx/bulk-rename.png
/usr/share/gtk-doc/html/thunarx/home.png
/usr/share/gtk-doc/html/thunarx/index.html
/usr/share/gtk-doc/html/thunarx/ix01.html
/usr/share/gtk-doc/html/thunarx/left-insensitive.png
/usr/share/gtk-doc/html/thunarx/left.png
/usr/share/gtk-doc/html/thunarx/menu-provider.png
/usr/share/gtk-doc/html/thunarx/right-insensitive.png
/usr/share/gtk-doc/html/thunarx/right.png
/usr/share/gtk-doc/html/thunarx/say-hello.png
/usr/share/gtk-doc/html/thunarx/style.css
/usr/share/gtk-doc/html/thunarx/thunarx-Variables-and-functions-to-check-the-library-version.html
/usr/share/gtk-doc/html/thunarx/thunarx-abstraction-layer.html
/usr/share/gtk-doc/html/thunarx/thunarx-fundamentals.html
/usr/share/gtk-doc/html/thunarx/thunarx-overview.html
/usr/share/gtk-doc/html/thunarx/thunarx-providers.html
/usr/share/gtk-doc/html/thunarx/thunarx-using-extensions.html
/usr/share/gtk-doc/html/thunarx/thunarx-writing-extensions-advanced-topics.html
/usr/share/gtk-doc/html/thunarx/thunarx-writing-extensions-getting-started.html
/usr/share/gtk-doc/html/thunarx/thunarx-writing-extensions.html
/usr/share/gtk-doc/html/thunarx/thunarx.devhelp2
/usr/share/gtk-doc/html/thunarx/up-insensitive.png
/usr/share/gtk-doc/html/thunarx/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libthunarx-3.so.0
/usr/lib64/libthunarx-3.so.0.0.0
/usr/lib64/thunarx-3/thunar-apr.so
/usr/lib64/thunarx-3/thunar-sbr.so
/usr/lib64/thunarx-3/thunar-uca.so
/usr/lib64/thunarx-3/thunar-wallpaper-plugin.so
/usr/lib64/xfce4/panel/plugins/libthunar-tpa.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Thunar/86207ea3fdd7e8ef5ea34ca9d12a511dc7272d31
/usr/share/package-licenses/Thunar/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/Thunar.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/thunar.service

%files locales -f thunar.lang
%defattr(-,root,root,-)

