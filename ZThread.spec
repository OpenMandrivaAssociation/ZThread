%define	name		ZThread
%define	version		2.3.1
%define	release		2mdk
%define	lib_name_orig	lib%{name}
%define	lib_major	1
%define	lib_name        %mklibname %{name} %{lib_major}
#(peroyvind) for some reason when using this, something gets screwed up..
#%define	lib_name_devel	%mklibname %{name} %{lib_major} -d
#%define	lib_name_static_devel	%mklibname %{name} %{lib_major} -s -d

Name:           %{name}
Version:        %{version}
Release:        %{release}
Source0:	%{name}-%{version}.tar.bz2
License:	LGPL
Group:		System/Libraries
URL:		http://zthread.sourceforge.net/
Summary:	Cross-platform C++ multi-threading framework
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	automake >= 1.7
%description
%name is an advanced platform-independent, Object-Oriented threading and
synchronization library. It has been designed and tested under POSIX & Win32
systems. It is not just another thread wrapper.

%package -n	%{lib_name}
Summary:	Libraries needed by %name
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{lib_name}
%name is an advanced platform-independent, Object-Oriented threading and
synchronization library. It has been designed and tested under POSIX & Win32
systems. It is not just another thread wrapper. 

%package -n	%{lib_name}-devel
Summary:	Development tools for %name
Group:		Development/C++
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{lib_name}-devel
This package contains the development libraries and header files
needed for development with %name.

%package -n	%{lib_name}-static-devel
Summary:	ZThread static library
Group:		Development/C++
Requires:	%{lib_name}-devel = %{version}
Provides:	%{lib_name_orig}-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n	%{lib_name}-static-devel
%name static library.

%package -n	%{lib_name}-doc
Summary:	HTML formatted API documention for %name
Group:		Development/Other
Requires:       %{lib_name} = %{version}

%description -n	%{lib_name}-doc
This package contains HTML formatted API documention generated by
the popular doxygen documentation generation tool.

%prep
%setup -q

%build
CXXFLAGS="$RPM_OPT_FLAGS -fpermissive" \
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/lib*.so.*
%doc AUTHORS NEWS README TODO ChangeLog

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4

%files -n %{lib_name}-static-devel
%defattr(-,root,root)
%{_libdir}/*.*a

%files -n %{lib_name}-doc
%defattr(-,root,root)
%doc doc/*
