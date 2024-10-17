Name:		texlive-pst-marble
Version:	50925
Release:	2
Summary:	A PSTricks package to draw marble-like patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-marble
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-marble.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-marble.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a PSTricks package to draw marble-like patterns.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-marble
%{_texmfdistdir}/tex/generic/pst-marble
%{_texmfdistdir}/dvips/pst-marble
%doc %{_texmfdistdir}/doc/generic/pst-marble

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
