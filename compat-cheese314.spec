Name:           compat-cheese314
Version:        3.14.2
Release:        1%{?dist}
Summary:        Compat package with cheese 3.14 libraries

License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Cheese
Source0:        https://download.gnome.org/sources/cheese/3.14/cheese-%{version}.tar.xz

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libXtst-devel
BuildRequires:  vala-devel
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gst-2.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  /usr/bin/xsltproc

# Explicitly conflict with older cheese packages that ship libraries
# with the same soname as this compat package
Conflicts: cheese-libs < 2:3.18

%description
Compatibility package with cheese 3.14 librarires.


%prep
%setup -q -n cheese-%{version}


%build
%configure --disable-static
make V=1 %{?_smp_mflags}


%install
%make_install

rm -f %{buildroot}%{_libdir}/libcheese.{a,la}
rm -f %{buildroot}%{_libdir}/libcheese-gtk.{a,la}

rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/girepository-1.0/
rm -rf %{buildroot}%{_libdir}/pkgconfig/
rm -rf %{buildroot}%{_libdir}/*.so
rm -rf %{buildroot}%{_libexecdir}
rm -rf %{buildroot}%{_datadir}

chrpath --delete %{buildroot}%{_libdir}/libcheese-gtk.so.*


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%{_libdir}/libcheese.so.*
%{_libdir}/libcheese-gtk.so.*


%changelog
* Thu Oct 20 2016 Kalev Lember <klember@redhat.com> - 3.14.2-1
- Initial cheese 3.14 compat package
