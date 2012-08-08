# revision 26551
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-nicefilelist
Version:	20120808
Release:	1
Summary:	TeXLive nicefilelist package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicefilelist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicefilelist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicefilelist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive nicefilelist package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nicefilelist/nicefilelist.RLS
%{_texmfdistdir}/tex/latex/nicefilelist/nicefilelist.sty
%doc %{_texmfdistdir}/doc/latex/nicefilelist/README
%doc %{_texmfdistdir}/doc/latex/nicefilelist/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/nicefilelist/nicefilelist.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nicefilelist/empty.f
%doc %{_texmfdistdir}/source/latex/nicefilelist/nicefilelist.tex
%doc %{_texmfdistdir}/source/latex/nicefilelist/provonly.fd
%doc %{_texmfdistdir}/source/latex/nicefilelist/srcfiles.tex
%doc %{_texmfdistdir}/source/latex/nicefilelist/wrong.prv

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
