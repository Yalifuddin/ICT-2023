from django.forms import ModelForm
from . import models


class PendaftaranValorantForm(ModelForm):
    class Meta:
        model = models.PendaftaranValorant
        fields = ['Nama_Tim', 'Nomor_Whatsapp_dan_Line', 'Player_1', 'Nama_Lengkap_atau_Nama_Asli_1', 'Player_2', 'Nama_Lengkap_atau_Nama_Asli_2', 'Player_3', 'Nama_Lengkap_atau_Nama_Asli_3',
                  'Player_4', 'Nama_Lengkap_atau_Nama_Asli_4', 'Player_5', 'Nama_Lengkap_atau_Nama_Asli_5', 'Player_6', 'Nama_Lengkap_atau_Nama_Asli_6', 'Bukti_Transaksi']

    def __init__(self, *args, **kwargs):
        super(PendaftaranValorantForm, self).__init__(*args, **kwargs)
        self.fields['Nama_Tim'].widget.attrs.update(
            {'placeholder': 'Nama Tim', 'id': 'Nama_Tim'})
        self.fields['Nomor_Whatsapp_dan_Line'].widget.attrs.update(
            {'placeholder': 'Nomor Whatsapp dan Line', 'id': 'Kontak'})
        self.fields['Player_1'].widget.attrs.update(
            {'placeholder': 'Player 1 (ex. ICT #1234)', 'id': 'Player1'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_1'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli', 'id': 'Nama_Lengkap'})
        self.fields['Player_2'].widget.attrs.update(
            {'placeholder': 'Player 2 (ex. ICT #1234)', 'id': 'Player2'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_2'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli', 'id': 'Nama_Lengkap'})
        self.fields['Player_3'].widget.attrs.update(
            {'placeholder': 'Player 3 (ex. ICT #1234)', 'id': 'Player3'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_3'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli', 'id': 'Nama_Lengkap'})
        self.fields['Player_4'].widget.attrs.update(
            {'placeholder': 'Player 4 (ex. ICT #1234)', 'id': 'Player4'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_4'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli', 'id': 'Nama_Lengkap'})
        self.fields['Player_5'].widget.attrs.update(
            {'placeholder': 'Player 5 (ex. ICT #1234)', 'id': 'Player5'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_5'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli', 'id': 'Nama_Lengkap'})
        self.fields['Player_6'].widget.attrs.update(
            {'placeholder': 'Player 6 (cadangan)', 'id': 'Player6'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_6'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli', 'id': 'Nama_Lengkap'})
        self.fields['Bukti_Transaksi'].widget.attrs.update(
            {'placeholder': 'Bukti Transaksi'})


class PendaftaranShortMovieForm(ModelForm):
    class Meta:
        model = models.PendaftaranShortMovie
        fields = ['Nama_Tim', 'Asal_Sekolah', 'Nama_Perwakilan', 'Nomor_Whatsapp_dan_Line', 'Nama_Anggota', 'Bukti_Transaksi']

    def __init__(self, *args, **kwargs):
        super(PendaftaranShortMovieForm, self).__init__(*args, **kwargs)
        self.fields['Nama_Tim'].widget.attrs.update(
            {'placeholder': 'Nama Tim', 'id': 'Nama_Tim'})
        self.fields['Asal_Sekolah'].widget.attrs.update(
            {'placeholder': 'Asal Sekolah', 'id': 'Asal_Sekolah'})
        self.fields['Nama_Perwakilan'].widget.attrs.update(
            {'placeholder': 'Nama Perwakilan', 'id': 'Nama_Perwakilan'})
        self.fields['Nomor_Whatsapp_dan_Line'].widget.attrs.update(
            {'placeholder': 'Nomor Whatsapp dan Line', 'id': 'Kontak'})
        self.fields['Nama_Anggota'].widget.attrs.update(
            {'placeholder': 'Nama Anggota [ Pisahkan dengan tanda koma (,) ] ', 'id': 'Nama_Anggota'})
        self.fields['Bukti_Transaksi'].widget.attrs.update(
            {'placeholder': 'Bukti Transaksi'})

class PendaftaranPosterForm(ModelForm):
    class Meta:
        model = models.PendaftaranPoster
        fields = ['Nama', 'Asal_Sekolah',
                  'Nomor_Whatsapp_dan_Line', 'Bukti_Transaksi',]

    def __init__(self, *args, **kwargs):
        super(PendaftaranPosterForm, self).__init__(*args, **kwargs)
        self.fields['Nama'].widget.attrs.update(
            {'placeholder': 'Nama Kelompok', 'id': 'Nama_Lengkap'})
        self.fields['Asal_Sekolah'].widget.attrs.update(
            {'placeholder': 'Asal Sekolah', 'id': 'Asal_Sekolah'})
        self.fields['Nomor_Whatsapp_dan_Line'].widget.attrs.update(
            {'placeholder': 'Nomor Whatsapp dan Line', 'id': 'Kontak'})
        self.fields['Bukti_Transaksi'].widget.attrs.update(
            {'placeholder': 'Bukti Transaksi'}) 
