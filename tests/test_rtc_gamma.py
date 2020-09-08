from datetime import datetime

from hyp3_metadata import create


# FIXME: use tmp_path
def test_create_rtc_gamma_readme(tmp_path, test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    payload = create.marshal_metadata(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        looks=1,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    output_file = create.create_readme(payload)

    assert output_file.exists()


# FIXME: use tmp_path
def test_exact_rtc_gamma_product(test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    payload = create.marshal_metadata(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        looks=1,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    output_file_list = create.create_product_xmls(payload)
    for output_file in output_file_list:
        assert output_file.exists()


# FIXME: use tmp_path
def test_create_dem_xml(tmp_path, test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    payload = create.marshal_metadata(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        looks=1,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    output_file = create.create_dem_xml(payload)

    assert output_file.exists()


# FIXME: use tmp_path
def test_create_greyscale_browse_xml(tmp_path, test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    payload = create.marshal_metadata(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        looks=1,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    output_file = create.create_browse_xml(payload)

    assert output_file.exists()


# FIXME: use tmp_path
def test_exact_rtc_gamma_inc_map(test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    payload = create.marshal_metadata(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        looks=1,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    output_file = create.create_inc_map_xml(payload)

    assert output_file.exists()


# FIXME: use tmp_path
def test_exact_rtc_gamma_ls_map(test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    payload = create.marshal_metadata(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        looks=1,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    output_file = create.create_ls_map_xml(payload)

    assert output_file.exists()


def test_rtc_gamma_all_files(test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    files = create.create_metadata_file_set(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        looks=1,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    for f in files:
        assert f.exists()


def test_thumbnail_no_such_reference_file(test_data_folder):
    reference_file = test_data_folder / 'no_such_file'
    assert create.get_thumbnail_binary_string(reference_file) == b''


def test_thumbnail_reference_file_is_browse(test_data_folder):
    basename = 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    reference_file = test_data_folder / basename / f'{basename}.png'
    binary_string = create.get_thumbnail_binary_string(reference_file)
    assert len(binary_string) == 844


def test_thumbnail_reference_file_is_pol(test_data_folder):
    basename = 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    reference_file = test_data_folder / basename / f'{basename}_VV.png'
    binary_string = create.get_thumbnail_binary_string(reference_file)
    assert len(binary_string) == 844


def test_thumbnail_reference_file_is_dem(test_data_folder):
    basename = 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    reference_file = test_data_folder / basename / f'{basename}_dem.tif'
    binary_string = create.get_thumbnail_binary_string(reference_file)
    assert len(binary_string) == 844
