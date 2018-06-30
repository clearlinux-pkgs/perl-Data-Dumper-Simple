#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Dumper-Simple
Version  : 0.11
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/O/OV/OVID/Data-Dumper-Simple-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OV/OVID/Data-Dumper-Simple-0.11.tar.gz
Summary  : Easily dump variables with names
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Data-Dumper-Simple-man

%description
Data::Dumper::Simple version 0.10
=====================
INSTALLATION
To install this module type the following:

%package man
Summary: man components for the perl-Data-Dumper-Simple package.
Group: Default

%description man
man components for the perl-Data-Dumper-Simple package.


%prep
%setup -q -n Data-Dumper-Simple-0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Data/Dumper/Simple.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Dumper::Simple.3